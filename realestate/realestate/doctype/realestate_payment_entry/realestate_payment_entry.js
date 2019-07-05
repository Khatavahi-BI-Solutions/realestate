// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('RealEstate Payment Entry', {
	refresh: function(frm) {
		frm.events.set_accounts(frm)
	},
	realestate_partner: function(frm) {
		frm.events.set_accounts(frm)
	},
	payment_type: function(frm) {
		frm.events.set_accounts(frm)
	},
	mode_of_payment: function(frm) {
		frm.events.set_accounts(frm)
	},
	set_accounts: function(frm) {
		frappe.call({
			method: "realestate.realestate.doctype.realestate_payment_entry.realestate_payment_entry.get_bank_cash_account",
			args: {
				"realestate_partner": frm.doc.realestate_partner,
				"payment_type": frm.doc.payment_type,
				"mode_of_payment": frm.doc.mode_of_payment,
				"company": frm.doc.company,
				"project": frm.doc.realestate_project
			},
			callback: function(r) {
				if(r.message) {
				}
			}
		});
	},
	setup: function(frm) {
		frm.set_query("account_paid_from", function() {
			var account_types = in_list(["Pay", "Internal Transfer"], frm.doc.payment_type) ?
				["Bank", "Cash"] : [frappe.boot.party_account_types["Shareholder"]];

			return {
				filters: {
					"account_type": ["in", account_types],
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
		frm.set_query("account_paid_to", function() {
			var account_types = in_list(["Receive", "Internal Transfer"], frm.doc.payment_type) ?
				["Bank", "Cash"] : [frappe.boot.party_account_types["Shareholder"]];

			return {
				filters: {
					"account_type": ["in", account_types],
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
	}
});
