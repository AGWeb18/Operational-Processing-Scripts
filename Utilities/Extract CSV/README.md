# Extract from CSVs
Pull specific records, across many CSV files, into a single CSV. 


## Getting Started
After you've downloaded the script, follow steps 1 to 4. 

###  Step 1
```py
#   1. Populate this list with what you want to extract
 extract_items = ["WHAT","YOU","WANT","TO","EXTRACT"]
```
 - In a list format, set the criteria you'd like a column filtered by. 

###  Step 2
```py
#   2. Change this to the column you want to filter by - be EXACT. 
extract_col = "COLUMN NAME GOES HERE"
```
 - Set the name of the column you want to filter by - all CSVs must have the same column names.  

###  Step 3
```py
#   3. Set this to where you've stored all the CSV files. 
file_path = (r"C:\\Users\\USERNAME\\Documents\\INPUT")
```
 - All the files you're processing must be in CSV for this script to work. Set this to the folder you've stored all the CSV's in. 

###  Step 4
```py
#   4. Set this to both the file path and file name (with '.csv') you want to create.  
    extract_df.to_csv(r"C:\\Users\\USERNAME\\Documents\\OUTPUT", mode='a', index=False, header=False)
```
 - Include the path, the file name and the extension. Your output file will need a header row manually included. 


## Warning
Always change the output filename whenever you're running this script. 'Append' mode is on, which means new records will be added to the bottom of the output csv rather than the file being overwritten. 

When handling large data, this can easily be missed and throw off all your work. 

If you change the filename, you're completely safe.
