#   import packages
from os import listdir
import pandas as pd

#   User Defined path 
file_path = str(r"C:\\Users\\PATH\\TO\\REPORT\\")
files_in_directory = listdir(r"C:\\Users\\PATH\\TO\\REPORT\\")

#   Set up the header row - need to append later
l_of_cols= [
'row_number',
'dealer_customer_number',
'dealer_name',
'sales_rep_first_name',
'sales_rep_last_name',
'sales_rep_contact_id',
'end_user_customer_business_name',
'end_user_first_name',
'end_user_last_name',
'end_user_customer_address_line1',
'end_user_customer_address_line2',
'end_user_customer_address_city',
'end_user_customer_address_state',
'end_user_customer_address_zip',
'end_user_contact_info',
'sic_code',
'sic_code_description',
'end_user_price',
'date_of_sale',
'invoice_number_from_partner_to_end_user',
'div_cd',
'country_code',
'purchasedthroughlease',
'msi_invoice_number_to_partner',
'model_number_or_sku',
'model_description',
'apc_code',
'item_type',
'model_active_or_inactive_data',
'last_ship_date_if_in_active',
'msi_invoice_price_to_partner',
'serial_number',
'date_of_allocation_in_sales_view',
'date_of_issue_from_msi_to_vendor_or_360incentives',
'system_configuration',
'commercial_system_name',
'commercial_system_id',
'program_code',
'program_name',
'status',
'amount',
'reason']

#   format header row (transpose)
cols = pd.DataFrame(l_of_cols)
cols = cols.T

#   Append first row to new CSV
cols.to_csv(r"C:\\Users\\PATH\\TO\\REPORT\\OUTPUT\\CLEAN"), mode = 'a', header=False, index=False)

#   For each file in a directory
#   Split into 1 row chunks
#   Set up conditionals. 
for file in files_in_directory:

    df = pd.read_csv(file_path + file, chunksize=1)
    for chunk in df:
        status = chunk.iloc[:,39].item()
        if len(chunk.columns) == 42 and ((status=="Rejected") or (status =="Approved") or (status=="Declined") or (status=="Submitted") or status==("Not Processed") or status==("On Hold")):
            chunk.to_csv(r"C:\\Users\\PATH\\TO\\REPORT\\OUTPUT\\CLEAN\\"), mode = 'a', header=False, index=False)
        else:
            print("The file: " + str(file) + " has a line which didn't meet criteria. ")
            chunk.to_csv(r"C:\\Users\\PATH\\TO\\REPORT\\OUTPUT\\MESSY\\", mode = 'a', header=False, index=False)
