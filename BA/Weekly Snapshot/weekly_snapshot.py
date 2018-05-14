import pandas as pd
import os

#   Simply adjust these paths and run the script!

#   SRC represents the Source data
#   All files in this folder will be processed (aka - only store the files you want processed)
SRC_FILE_PATH = str("<PATH\\TO\\SOURCE\\FOLDER>")

#   DST represents the Destination data.
DST_FILE_PATH = str("<PATH\\TO\\DESTINATION\\FOLDER\\>")
DST_FILE_NAME = "NAME_OF_OUTPUT_FILE.csv"

#   Column headers go here
col_1 = "SalesReps"
col_2 = "SalesManager"
col_3 = "FileName"

#   User SRC path successfully pointed if printed
print("Processing ...")


#   Creates a list of columns headers
l_of_column_headers = [col_1, col_2, col_3]
df_header = pd.DataFrame(l_of_column_headers)
df_header = df_header.T


#   Add first row - header row
df_header.to_csv(DST_FILE_PATH + DST_FILE_NAME, mode='a',header=False, index=False)


for file_name in os.listdir(SRC_FILE_PATH):
    print(file_name)

    #   Read in the raw data source
    raw_data = pd.read_csv(SRC_FILE_PATH + file_name, encoding="latin-1")

    for i in range(0, len(raw_data)):
    #   Loop through the rows of the file
    #   Store the Sales Mgr + list of Sales Reps
    #   Create df of Sales Reps
    #   Add Sales Mgr column
    #   Drop NA's
    #   Append to csv.
        row_data = raw_data.iloc[i,:]
        sales_mgr = row_data[0]
        sr = row_data[1:]
        cleanedList = [x for x in sr if x != 'NaN']
        sr_series = pd.Series(cleanedList)
        df_group = pd.DataFrame(sr_series, columns=['Sales Rep'])
        df_group["Manager"] = sales_mgr
        df_group["File Name"] = file_name
        df_group = df_group.dropna(axis=0, how='any')
        df_group.to_csv(DST_FILE_PATH + DST_FILE_NAME, mode='a',header=False, index=False)

print("Completed!")
