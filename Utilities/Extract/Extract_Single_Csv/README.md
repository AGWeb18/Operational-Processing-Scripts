##  Extract Single CSV

Use this script to extract rows from a single CSV, based on a column value, regardless of how large it is. 



##  Setup
- Locate the file and file path you want to extract from. 
- Set up a comma separated list of the values you want to filter. 
- Enter the column name to search in. BE EXACT. 


## Warning
Always change the output filename whenever you're running this script. 'Append' mode is on (``` mode='a' ```) which means new records will be added to the bottom of the output csv rather than the file being overwritten.

When handling large data, this can easily be missed and throw off all your work.

If you change the filename, you're completely safe.
