# RealEstate
## Master Doctype
### Project
- It may provide the functionality of particular project may conduct how may investors and their percentage ration as per project
- Fields are as bellow used in doc.RealEstate Settings
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Project Name  | data | project_name | 
  | RealEstate Partner  | table | realestate_partner | RealEstate Project Partner
  | RealEstate Assets  | table | realestate_assets | RealEstate Assets
        
### RealEstate Project Partner(Child Table) 
- This is the middleware table which hold the data of real estate partner details
- Fields are as bellow used in 
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Partner  | link | partner | RealEstate Partner
  | Invested Amount  | currency |invested_amount  |    

### RealEstate Partner 
- which is link on Real Essets Project Partner
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Partner | data | partner_name | 
  | User | Link | user | User
  | Date | Date | date | 
### RealEstate Assets(Child Table)
- This is a child table that may describe the how much amount is invested in to particular project by investors.
- Fields are as bellow used in doc.RealEstate Assets(Child Table)
- | Lable | Type | Name | Options |
  |-------|------|-------|--------|
  | Assets Id  | int | assets_id | 
  | Item  | link | item | Item

### RealEstate Settings
- Fields are as bellow used in doc.RealEstate Settings
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Enable RealEstate  | check | enable_realestate | 
         
