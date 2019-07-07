// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('RealEstate Assets', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){

			frm.add_custom_button(__("Sales Invoice"), function(){
				//perform desired action such as routing to new form or fetching etc.
				frappe.model.open_mapped_doc({
					method: "realestate.realestate.doctype.realestate_assets.realestate_assets.make_sales_invoice",
					frm: cur_frm
				})
			}, __("Make"));
		}
	}
});
