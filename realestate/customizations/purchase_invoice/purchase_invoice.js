frappe.ui.form.on('Purchase Invoice Item', {
	item_code: function(frm, cdt, cdn){
		debugger;
		var child = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, 'project', frm.doc.project_reference)
	}
})