# Real Estate
## Master Doctype
### Project
- It may provide the functionality of particular project may conduct how may investors and their percentage ration as per project
- Fields are as bellow used in doc.Real Estate Settings
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Project Name  | data | project_name | 
  | Real Estate Partner  | table | real_estate_partner | Real Estate Project Partner
  | Real Estate Assets  | table | real_estate_assets | Real Estate Assets
        
### Real Estate Project Partner(Child Table) 
- This is the middleware table which hold the data of real estate partner details
- Fields are as bellow used in 
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Partner  | link | partner | Real Estate Partner
  | Invested Amount  | currency |invested_amount  |    

### Real Estate Partner 
- which is link on Real Essets Project Partner
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Partner | data | partner_name | 
  | User | Link | user | User
  | Date | Date | date | 
### Real Estate Assets(Child Table)
- This is a child table that may describe the how much amount is invested in to particular project by investors.
- Fields are as bellow used in doc.Real Estate Assets(Child Table)
- | Lable | Type | Name | Options |
  |-------|------|-------|--------|
  | Assets Id  | int | assets_id | 
  | Item  | link | item | Item

### Real Estate Settings
- Fields are as bellow used in doc.Real Estate Settings
- | Lables | Type | Name | Options |
  |-------|------|-------|--------|
  | Enable Real Estate  | check | enable_real_estate | 
         
