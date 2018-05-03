```py
#   import packages
from os import listdir
import pandas as pd

#   User Defined path 
file_path = str(r"C:\Users\<USERPATH>\")
files_in_directory = listdir(file_path)


#	Place Acceptable status'
acceptable_status_codes = ["Rejected","Approved","Declined", "Submitted", "Not Processed", "On Hold"]


#   For each file in a directory
#   Split into 1 row chunks
#   Set up conditionals. 
for file in files_in_directory:
	try:
		df = pd.read_csv(file_path + file, encoding='latin-1') #	invalid continuation byte error due to encoding type
		print("successful")
	except:
		print(file)
```
