# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class RealEstateProject(Document):

	def validate(self):
		self.update_outstanding()
	
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
		paid_entry = frappe.get_all('RealEstate Payment Entry', 
			filters={
				'docstatus': 1, 
				'payment_type': 'Receive',
				'realestate_partner': partner_row.partner, 
				'realestate_project': self.name
			}, 
			fields=['paid_amount']
		)
		paid_amount = 0
		for entry in paid_entry:
			paid_amount += float(entry['paid_amount'])
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
				"project": "project"
			}
		}}, target_doc)

	return doclist