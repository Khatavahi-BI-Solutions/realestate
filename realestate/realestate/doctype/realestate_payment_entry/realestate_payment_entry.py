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
		doc = frappe.get_doc({
			"doctype": "Journal Entry",
			"voucher_type": "Journal Entry",
		})
		if self.payment_type == "Pay":
			#from
			doc.append("accounts", {
				"account":self.account_paid_from,
				"credit_in_account_currency": self.paid_amount
			})
			#to
			doc.append("accounts", {
				"account": self.account_paid_to,
				"party": self.shareholder,
				"debit_in_account_currency":self.paid_amount
			})
		else:
			#to
			doc.append("accounts", {
				"account":self.account_paid_to,
				"debit_in_account_currency": self.paid_amount
			})
			#from
			doc.append("accounts", {
				"account": self.account_paid_from,
				"party": self.shareholder,
				"credit_in_account_currency":self.paid_amount
			})
		for row in doc.accounts:
				print(row.account)
		doc.insert()
		doc.submit()
	
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
			account['to'] = frappe.get_value("Mode of Payment Account", filters = { "parent":mode_of_payment, "company":company}, fieldname = "default_account")
		if not account['to']:
			account['to'] = frappe.get_value("RealEstate Settings", "RealEstate Settings", "account_receivable")
	else:
		#pay
		account['to'] = frappe.get_value("RealEstate Partner", realestate_partner, "account")
		if not account['to']:
			account['to'] = frappe.get_value("RealEstate Settings", "RealEstate Settings", "account_payable")
		
		account['from'] = frappe.get_value("RealEstate Project", project, "account_receivable")
		if not account['from']:
			account['from'] = frappe.get_value("Mode of Payment Account", filters = { "parent":mode_of_payment, "company":company}, fieldname = "default_account")
		if not account['from']:
			account['from'] = frappe.get_value("RealEstate Settings", "RealEstate Settings", "account_receivable")
	
	return account
