import pandas as pd

#   Simply adjust these paths and run the script!
#   SRC represents the Source data.
SRC_FILE_PATH = str("C:\\Users\\<USERNAME>\\Desktop\\")
SRC_FILE_NAME = "FILENAME_IN.csv"

#   DST represents the Destination data.
DST_FILE_PATH = str("C:\\Users\\<USERNAME>\\Desktop\\")
DST_FILE_NAME = "FILENAME_OUT.csv"

#   Column headers go here
col_1 = "COLUMN_HEADER_1"
col_2 = "COLUMN_HEADER_2"

#   User SRC path successfully pointed if printed
print("Processing ...")


#   Creates a list of columns headers
l_of_column_headers = [col_1, col_2]
df_header = pd.DataFrame(l_of_column_headers)
df_header = df_header.T


#   Read in the raw data source
raw_data = pd.read_csv(SRC_FILE_PATH + SRC_FILE_NAME)


#   Add first row - header row
df_header.to_csv(DST_FILE_PATH + DST_FILE_NAME, mode='a',header=False, index=False)


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
    df_group = df_group.dropna(axis=0, how='any')
    df_group.to_csv(DST_FILE_PATH + DST_FILE_NAME, mode='a',header=False, index=False)

print("Completed!")
