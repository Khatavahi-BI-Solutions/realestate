# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

class RealEstateSettings(Document):
	def validate(self):
		if self.enable_realestate == 1:
			# setup_custom_fields()
			pass

@frappe.whitelist()
def setup_custom_fields():
	custom_fields = {
		"Project": [
			dict(
				fieldname='realestate_project_details',
				label='RealEstate Project Details ',
				fieldtype='Section Break',
				insert_after='sales_order'
			),
			dict(
				fieldname='realestate_project',
				label='RealEstate Project',
				fieldtype='Link',
				options='RealEstate Project',
				insert_after='realestate_project_details',
			),		
		]
	}

	create_custom_fields(custom_fields)
	frappe.msgprint("Custome Field update done.")