// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('RealEstate Settings', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){

			frm.add_custom_button(__('Update Custome Field'), function() {
				frappe.call({
					method:"realestate.realestate.doctype.realestate_settings.realestate_settings.setup_custom_fields",
				})
			}).addClass("btn-primary");
		}
	},
	setup: function(frm) {
		frm.set_query("account_payable", function() {
			return {
				filters: {
					"account_type": ["in", "Payable"],
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
		frm.set_query("account_receivable", function() {
			return {
				filters: {
					"account_type": ["in", ["Bank", "Cash"]],
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
	}
});
