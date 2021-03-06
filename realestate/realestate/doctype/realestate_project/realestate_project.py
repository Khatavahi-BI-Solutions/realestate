# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class RealEstateProject(Document):

	def validate(self):
		pass
		
	def on_update(self):
		self.update_outstanding()
		self.calculate_capital()
		self.update_costing()
		self.update_account_receivable_payable()
		self.update_assets()
	
	def onload(self):
		self.update_outstanding()
		self.calculate_capital()
		self.update_costing()
		self.update_account_receivable_payable()
		self.update_assets()

	def update_assets(self):
		for asset in self.realestate_assets:
			assets = frappe.get_doc("RealEstate Assets", asset.asset)
			asset.status = assets.asset_status
			asset.rate = assets.rate
			asset.amount = assets.total_amount
			asset.outstanding = assets.total_outstanding

	def update_costing(self):
		total_sales_amount = frappe.db.sql("""select sum(base_net_total)
			from `tabSales Invoice` where project = %s and docstatus=1""", self.project)

		self.total_revenue = total_sales_amount and total_sales_amount[0][0] or 0

		total_purchase_cost = frappe.db.sql("""select sum(base_net_amount)
			from `tabPurchase Invoice Item` where project = %s and docstatus=1""", self.project)

		self.total_expenses = total_purchase_cost and total_purchase_cost[0][0] or 0

		self.profit = self.total_revenue - self.total_expenses
	
	def update_account_receivable_payable(self):
		total_receivable = frappe.db.sql("""select sum(outstanding_amount)
			from `tabSales Invoice` where project = %s and docstatus=1""", self.project)

		self.accounts_receivable = total_receivable and total_receivable[0][0] or 0

		total_payable = frappe.db.sql("""
			select sum(outstanding_amount) from (select pi.outstanding_amount as outstanding_amount
				from `tabPurchase Invoice` as pi inner join
				`tabPurchase Invoice Item` as pit on pi.name = pit.parent
				where pit.project = %s and pi.docstatus=1 group by pi.name) pi""", self.project)
		
		self.accounts_payable = total_payable and total_payable[0][0] or 0

		self.current_balance = self.capital + \
								self.total_revenue - \
								self.accounts_receivable - \
								self.total_expenses + \
								self.accounts_payable
	
	def calculate_capital(self):
		capital_payment = frappe.get_all(
			'RealEstate Payment Entry', 
			filters={
				'realestate_project': self.name, 
				'docstatus':'1'
			},
			fields=['payment_type', 'paid_amount']
		
		)
		capital = 0
		for row in capital_payment:
			if row['payment_type'] == 'Receive':
				capital += row['paid_amount']
			if row['payment_type'] == 'Pay':
				capital -= row['paid_amount']

		self.capital = capital

	def after_insert(self):
		if not self.project:
			self.create_project(True)
	
	def before_remove(self):
		if self.project:
			self.project=""
			self.save()
			return "Project Unlinked"

	def create_project(self, from_after_insert = False):
		if frappe.db.get_value("Project", self.project_name, "name"):
			project = frappe.get_doc("Project",self.project_name)
		else:
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": self.project_name,
				"real_estate_project": self.name
			})
			project.save()
		self.project = project.name
		if not from_after_insert:
			self.save()
	
	def delete_project(self, project):
		frappe.delete_doc("Project", project)

	def update_outstanding(self):
		for partner_row in self.partner:
			partner_row.outstanding_amount = partner_row.invested_amount - self.get_paid_amount(partner_row)
	
	def get_paid_amount(self, partner_row):
		paid_entry = frappe.get_all(
			'RealEstate Payment Entry', 
			filters={
				'realestate_project': self.name,
				'realestate_partner': partner_row.partner,
				'docstatus':'1'
			},
			fields=['payment_type', 'paid_amount']
		
		)
		paid_amount = 0
		for row in paid_entry:
			if row['payment_type'] == 'Receive':
				paid_amount += row['paid_amount']
			if row['payment_type'] == 'Pay':
				paid_amount -= row['paid_amount']
		return paid_amount

@frappe.whitelist()
def make_sales_invoice(source_name, target_doc=None):

	doclist = get_mapped_doc("RealEstate Project", source_name,
		{"RealEstate Project": {
			"doctype": "Sales Invoice",
			"field_map": {
				"project": "project"
			}
		}}, target_doc)

	return doclist

@frappe.whitelist()
def make_purchase_invoice(source_name, target_doc=None):

	doclist = get_mapped_doc("RealEstate Project", source_name,
		{"RealEstate Project": {
			"doctype": "Purchase Invoice",
			"field_map": {
				"project": "project_reference"
			}
		}}, target_doc)

	return doclist

@frappe.whitelist()
def make_payment_entry(source_name, target_doc = None):

	doclist = get_mapped_doc("RealEstate Project", source_name,
		{"RealEstate Project": {
			"doctype": "RealEstate Payment Entry",
			"field_map": {
				"name": "realestate_project"
			}
		}}, target_doc)

	return doclist