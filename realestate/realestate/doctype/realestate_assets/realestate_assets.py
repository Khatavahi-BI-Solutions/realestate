# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class RealEstateAssets(Document):
	def validate(self):
		realestate_settings = frappe.get_doc("RealEstate Settings", "RealEstate Settings")
		if not self.item:
			self.create_item()
		else:
			item = frappe.get_doc("Item",self.item)
			self.update_item_description(item)
		# self.create_update_item_price(realestate_settings)
		self.update_invoice_details()
		self.total_calculation()
	
	def on_update(self):
		self.update_realestate_project()
	
	def update_realestate_project(self):
		project = frappe.get_all('RealEstate Assets Table', filters={'asset': self.name }, fields=['parent'])
		for pro in project:
			project = frappe.get_doc("RealEstate Project", pro.parent)
			project.save()
	
	def total_calculation(self):
		total_amount, total_outstanding = 0,0
		for row in self.sales_invoice:
			total_amount += row.amount
			total_outstanding += row.outstanding
		
		self.total_amount = total_amount
		self.total_outstanding = total_outstanding

	def create_item(self):
		if frappe.db.get_value("Item", self.assets_name, "name"):
			item = frappe.get_doc("Item",self.assets_name)
		else:
			item = frappe.get_doc({
				"doctype": "Item",
				"item_code": self.assets_name,
				"item_group": self.item_group,
				"description": self.assets_details
			})
			item.save()
		self.item = item.name
	
	def create_update_item_price(self, realestate_settings):
		if frappe.db.get_values("Item Price",filters={"item_code":self.item, "price_list":realestate_settings.price_list}, fieldname=["name"]):
			
			item_price = frappe.get_doc("Item Price",frappe.db.get_values("Item Price",filters={"item_code":self.item, "price_list":realestate_settings.price_list}, fieldname=["name"]))
			item_price.price_list_rate = self.price_list_rate
			item_price.save()
		else:
			
			item_price = frappe.get_doc({
				"doctype": "Item Price",
				"item_code": self.item,	
				"price_list": realestate_settings.price_list,
				"price_list_rate": self.price_list_rate
			})
			item_price.save()

	def update_item_description(self, item):
		item.description = self.assets_details
		item.save()
	
	def update_invoice_details(self):
		sales_invoice = frappe.get_all('Sales Invoice Item', filters={'docstatus': 1, 'item_code': self.item }, fields=['parent'])
		self.sales_invoice = {}
		invoice_exist = False
		for sin in sales_invoice:
			invoice_exist = True
			self.append('sales_invoice', {
				'sales_invoice': sin.parent,
				'amount': frappe.get_value("Sales Invoice", sin.parent, 'grand_total'),
				'outstanding': frappe.get_value("Sales Invoice", sin.parent, 'outstanding_amount')
			})
		if invoice_exist:
			self.asset_status = "Sold"
		else:
			self.asset_status = "Available"

@frappe.whitelist()
def make_sales_invoice(source_name, target_doc=None):

	doclist = get_mapped_doc("RealEstate Assets", source_name,
		{
			"RealEstate Assets": {
				"doctype": "Sales Invoice",
				"field_map": {
					"project": "project"
				}
			}
		}, target_doc)

	return doclist