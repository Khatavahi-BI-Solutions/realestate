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
	}
});
