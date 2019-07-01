// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('RealEstate Project', {
	refresh: function(frm) {
		frm.add_fetch("partner", "account_head", "account_head");
		if(!frm.doc.__islocal && frm.doc.project){
			var project = frm.doc.project;

			frm.add_custom_button(__("Sales Invoice"), function(){
				//perform desired action such as routing to new form or fetching etc.
			}, __("Make"));
			frm.add_custom_button(__("Purchase Invoice"), function(){
				//perform desired action such as routing to new form or fetching etc.
			}, __("Make"));
			frm.add_custom_button(__('Open Project'), function() {
				frappe.set_route("Form", "Project",frm.doc.project)
			}, __("Project") );
			// if(frappe.user.has_role("Administrator")){
			// 	frm.add_custom_button(__('Remove Project'), function() {
			// 		frappe.call({
			// 			doc: frm.doc,
			// 			method:'before_remove',
			// 			callback: function(r) {
							
			// 				frappe.call({
			// 					doc: frm.doc,
			// 					method:'delete_project',
			// 					args: {
			// 						"project":project
			// 					},
			// 					callback: function(r) {
			// 						show_alert('Project Deleted.')
			// 						location.reload();
			// 					}
			// 				})
			// 				show_alert('Project Unlinked.')
						
			// 			}
			// 		})
			// 	}, __("Project") );
			// }
		}
		if(!frm.doc.__islocal && !frm.doc.project){
			frm.add_custom_button(__('Create Project'), function() {
				frappe.call({
					doc: frm.doc,
					method:'create_project',
					callback: function(r) {
						show_alert('Project Created.')
						location.reload();
					}
				})
			}, __("Project"));
		}

		frm.add_custom_button(__('Calculate Partnership'), function() {
			frm.events.calculate_partnership(frm)
		}, __("Project"));
	},
	budget_amount: function(frm) {
		// frm.events.calculate_partnership(frm)
	},
	calculate_partnership: function(frm) {	
		if(frm.doc.budget_amount){
			frm.doc.partner.forEach(function(element) {
				console.log(element);
				var partnership = parseFloat(parseFloat(element.invested_amount).toFixed(2) * 100 / parseFloat(frm.doc.budget_amount).toFixed(2) ).toFixed(2);
				frappe.model.set_value(element.doctype, element.name, "partnership", partnership)
			});
		}  
	}
});
