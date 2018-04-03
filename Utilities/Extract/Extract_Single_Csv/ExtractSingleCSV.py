#   Extract SINGLE CSV - Python Script
################################

import pandas as pd


#   1. Populate this list with what you want to extract
extract_items = ["Items","To","Extract"]

#   2. Change this to the column you want to filter by - be EXACT. 
extract_col = "Column_Name"


#   3. Set this to where you've stored all the CSV files. 
file_path = (r"C://PATH/TO/THE/FILE/INPUT")


# Uncomment if English Client
temp_df = pd.read_csv(file_path, low_memory=False)

# Uncomment if Canadian(French)/Spanish Client
#temp_df = pd.read_csv(file_path, low_memory=False, encoding='latin-1')


extract_df = temp_df.loc[temp_df[extract_col].isin(extract_items)]
    
#   4. Set this to both the file path and file name (with '.csv') you want to create.  
extract_df.to_csv(r"PATH/TO/THE/FILE/OUTPUT", mode='a', index=False, header=False)
