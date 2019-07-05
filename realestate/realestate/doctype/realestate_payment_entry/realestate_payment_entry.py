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
		self.make_journal_voucher()
	
	def on_cancel(self):
		project = frappe.get_doc('RealEstate Project', self.realestate_project)
		project.save()
		self.cancel_journal_voucher()
	
	def make_journal_voucher(self):
		pass
	
	def cancel_journal_voucher(self):
		pass

@frappe.whitelist()
def get_bank_cash_account(realestate_partner = None, payment_type = None, mode_of_payment = None, company = None, project = None):
	account = {
		"to":"",
		"from":""
	}
	
	if payment_type == "Receive":
		account['from'] = frappe.get_value("RealEstate Partner", realestate_partner, "account")
		if not account['from']:
			account['from'] = frappe.get_value("RealEstate Settings", "RealEstate Settings", "account_payable")
		
		account['to'] = frappe.get_value("RealEstate Project", project, "account_receivable")
		if not account['to']:
			account['to'] = frappe.get_value("RealEstate Settings", "RealEstate Settings", "account_payable")
	else:
		pass
