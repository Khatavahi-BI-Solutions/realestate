import frappe

def sales_invoice_submit(doc, method = None):
	return
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def sales_invoice_cancel(doc, method = None):
	return
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def purchase_invoice_submit(doc, method = None):
	return
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def purchase_invoice_cancel(doc, method = None):
	return
	assets = []
	for item in doc.items:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def payment_entry_submit(doc, method):
	return
	assets = []
	for item in doc.references:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)

def payment_entry_cancel(doc, method):
	return
	assets = []
	for item in doc.references:
		asset = frappe.get_doc("RealEstate Assets",{"item": item.item_code})
		if asset not in assets:
			asset.save()
			assets.append(asset)
# def sales_order_submit(doc, method):
# 	pass

# def sales_order_cancel(doc, method):
# 	pass