#  Flatten Nested List

### Imagine you had many rows of data...

The first column is the parent. All other columns (of varying length) in the rows, are the children. 
This script builds a csv from these nested lists with their Child Parent relationships. 

### Code Example

```python

 #  By storing the index (first column) of the row as the Sales Mgr
 sales_mgr = row_data[0]
 
 #  and all others the Sales Rep
 sr = row_data[1:]
 
 #  We can create a Dataframe from the Sales Rep
 df_group = pd.DataFrame(sr_series, columns=['Sales Rep'])
 
  #  and add a column with the Sales Mgr
 df_group["Manager"] = sales_mgr
  
 
 #  We can drop rows if any Na's are found
 df_group = df_group.dropna(axis=0, how='any')
 
 #  And append to the DST csv. 
 df_group.to_csv(DST_FILE_PATH + DST_FILE_NAME, mode='a',header=False, index=False)

```

### Setup

The user will need to make sure the paths are correctly defined. 
This means if you want to use a new file or save it to a new folder, you'll need to adjust these values.

```python

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

```

### Running the Script

* Open the **nested_list_to_csv.py** file in IDLE (or your favourite IDE). 
* Ensure all paths are correctly defined
* Run the script (Press F5). 
