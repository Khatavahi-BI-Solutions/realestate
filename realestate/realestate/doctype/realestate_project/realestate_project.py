# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RealEstateProject(Document):
	def validate(self):
		realestate_settings = frappe.get_doc("RealEstate Settings", "RealEstate Settings")
		if not self.item:
			self.create_item()
		else:
			item = frappe.get_doc("Item",self.item)
			self.update_item_description(item)
		# self.create_update_item_price(realestate_settings)
	
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
