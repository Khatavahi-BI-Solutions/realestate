# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "realestate"
app_title = "RealEstate"
app_publisher = "Jigar Tarpara"
app_description = "Construction Businesse Management"
app_icon = "octicon octicon-file-directory"
app_color = "Yellow"
app_email = "khatavahi.tarparatech@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/realestate/css/realestate.css"
# app_include_js = "/assets/realestate/js/realestate.js"

# include js, css files in header of web template
# web_include_css = "/assets/realestate/css/realestate.css"
# web_include_js = "/assets/realestate/js/realestate.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "realestate.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "realestate.install.before_install"
# after_install = "realestate.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "realestate.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Sales Invoice": {
		"on_submit": "realestate.utils.sales_invoice_submit",
		"on_cancel": "realestate.utils.sales_invoice_cancel",
	},
	"Payment Entry": {
		"on_submit": "realestate.utils.payment_entry_submit",
		"on_cancel": "realestate.utils.payment_entry_cancel",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"realestate.tasks.all"
# 	],
# 	"daily": [
# 		"realestate.tasks.daily"
# 	],
# 	"hourly": [
# 		"realestate.tasks.hourly"
# 	],
# 	"weekly": [
# 		"realestate.tasks.weekly"
# 	]
# 	"monthly": [
# 		"realestate.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "realestate.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "realestate.event.get_events"
# }

doctype_js = {
	"Purchase Invoice" : "customizations/purchase_invoice/purchase_invoice.js",
	"Project" : "customizations/project/project.js",
}
