#   CLR AUDIT - Script
import pandas as pd


#   User defined path
SRC_FILE_PATH =str("C:\\Users\\ARidding\\Desktop\\Client Data\\Motorola\\CLR\\AuditData\\Zyme\\")
SRC_FILE_NAME ="ZYME_TO_360_10MAR20180710.txt"

CLR_FILE_PATH = str("C:\\Users\\ARidding\\Desktop\\Client Data\\Motorola\\CLR\\AuditData\\CLR\\")
CLR_FILE_NAME = "ZYME_TO_360_10MAR20180710_REPORT.csv"



#   Read in both Zyme and CLR report, of the same date. 
zyme_raw_data = pd.read_csv(SRC_FILE_PATH + SRC_FILE_NAME,sep='|')
clr_raw_data = pd.read_csv(CLR_FILE_PATH + CLR_FILE_NAME, sep=',')


#   Perform the value counts on Zyme vs CLR Invoice No
s_zyme_invoice = zyme_raw_data["Invoice number from partner to end-user"].value_counts()
s_clr_invoice = clr_raw_data["invoice_number_from_partner_to_end_user"].value_counts()


#   Convert to dataframe
df_zyme_invoice = pd.DataFrame(s_zyme_invoice, columns=["InvoiceNo-Zyme","Count-Zyme"])
df_clr_invoice = pd.DataFrame(s_clr_invoice, columns=["InvoiceNo-CLR","Count-CLR"])


#   


merge_results = pd.merge(df_zyme_invoice, df_clr_invoice, left_on='InvoiceNo-Zyme',right_on='InvoiceNo-CLR', how='outer')
print(merge_results)



#   Data Quality Checks
#   Missingness Checks
#   Total Count
#   Run Zyme against model, what it SHOULD be.


#print("==== FILE SUMMARY - ZYME AGAINST CLR ====")

#print("For File:" + SRC_FILE_NAME + " the total number of items is: " + str(len(zyme_raw_data)))
#print("For File:" + CLR_FILE_NAME + " the total number of items is: " + str(len(clr_raw_data)))
