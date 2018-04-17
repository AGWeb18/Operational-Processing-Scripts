# Extract from Core
Based on a Core export, extract paid claims for serialized models, for a specific dealer 

##  Getting Started
1. Configure the script to work on your machine.
```py
#   Set user-defined path- SRC and DST
SRC_PATH =r"C:\\Users\\<USERNAME>\\Documents\\SRC\\PATH\\"
SRC_NAME = "FILENAME_INPUT.csv"

DST_PATH = r"C:\\Users\\<USERNAME>\\Documents\\DST\\PATH\\"
DST_NAME = "FILENAME_OUTPUT.csv"
```

2.  Set the Dealer Name you want to extract
```py
#   Set Dealer Name
DEALER_NAME = "DEALER NAME GOES HERE"
```

3.  Confirm that the criteria is as-expected
```py
#   Filter Out based on conditions
raw_data = raw_data[raw_data["Dealer"] == DEALER_NAME]
raw_data = raw_data[raw_data["Status"] == "Paid"]
raw_data.dropna(subset=["Serial Number"], inplace=True)

```

### Set Up Complete - Run the Script
