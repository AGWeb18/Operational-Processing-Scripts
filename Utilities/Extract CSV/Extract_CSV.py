#   Extract CSV - Python Script
################################

import pandas as pd
import os


#   1. Populate this list with what you want to extract
extract_items = ["WHAT","YOU","WANT","TO","EXTRACT"]

#   2. Change this to the column you want to filter by - be EXACT. 
extract_col = "COLUMN NAME GOES HERE"


#   3. Set this to where you've stored all the CSV files. 
file_path = (r"C:\\Users\\USERNAME\\Documents\\INPUT")

for file_name in os.listdir(file_path):
    print("Working on: " + file_name)
    temp_df = pd.read_csv(file_path + file_name)
    extract_df = temp_df.loc[temp_df[extract_col].isin(extract_items)]
    
#   4. Set this to both the file path and file name (with '.csv') you want to create.  
    extract_df.to_csv(r"C:\\Users\\USERNAME\\Documents\\OUTPUT", mode='a', index=False, header=False)
