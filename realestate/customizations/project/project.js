frappe.ui.form.on('Project', {
	refresh: function(frm, cdt, cdn){
		frm.add_custom_button(__('Open RealEstate Project'), function() {
			frappe.set_route("Form", "RealEstate Project",frm.doc.name)
		}, __("RealEstate Project") );
	}
})