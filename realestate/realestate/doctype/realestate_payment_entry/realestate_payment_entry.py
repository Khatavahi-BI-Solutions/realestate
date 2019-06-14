# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RealEstatePaymentEntry(Document):
	def on_submit(self):
		project = frappe.get_doc('RealEstate Project', self.realestate_project)
		project.save()
	
	def on_cancel(self):
		project = frappe.get_doc('RealEstate Project', self.realestate_project)
		project.save()