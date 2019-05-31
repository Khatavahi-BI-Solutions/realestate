# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RealEstateProject(Document):
	def after_insert(self):
		if not self.project:
			self.create_project(True)
	
	def before_remove(self):
		if self.project:
			self.project=""
			self.save()
			return "Project Unlinked"

	def create_project(self, from_after_insert = False):
		if frappe.db.get_value("Project", self.project_name, "name"):
			project = frappe.get_doc("Project",self.project_name)
		else:
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": self.project_name,
				"real_estate_project": self.name
			})
			project.save()
		self.project = project.name
		if not from_after_insert:
			self.save()
	
	def delete_project(self, project):
		frappe.delete_doc("Project", project)