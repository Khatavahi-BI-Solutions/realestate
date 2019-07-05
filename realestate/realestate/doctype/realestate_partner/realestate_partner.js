// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('RealEstate Partner', {
	refresh: function(frm) {

	},
	setup: function(frm) {
		frm.set_query("account", function() {

			return {
				filters: {
					"account_type": ["in", "Payable"],
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
	}
});
