import frappe

def sales_invoice_submit(doc, method):
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def sales_invoice_cancel(doc, method):
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

# def sales_order_submit(doc, method):
# 	pass

# def sales_order_cancel(doc, method):
# 	pass