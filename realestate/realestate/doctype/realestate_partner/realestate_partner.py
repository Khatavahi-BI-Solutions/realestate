# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RealEstatePartner(Document):
	def validate(self):
		if not self.shareholder:
			self.create_shareholder()

	def create_shareholder(self):
		if frappe.db.get_value("Shareholder", self.partner_name, "name"):
			shareholder = frappe.get_doc("Shareholder",self.partner_name)
		else:
			shareholder = frappe.get_doc({
				"doctype": "Shareholder",
				"title": self.partner_name
			})
			shareholder.save()
		self.shareholder = shareholder.name
