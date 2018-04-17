#################################
#       YTD REPORTING           #
#       Paid Claims             #
#       Serial Numbers Only     #
#       For the Top 5 Dealers   #
#################################

#   Script was built off CORE export.
#   Column names may need to be modified. 


#   Import required packages
import pandas as pd

#   Set user-defined path- SRC and DST
SRC_PATH =r"C:\\Users\\<USERNAME>\\Documents\\SRC\\PATH\\"
SRC_NAME = "FILENAME_INPUT.csv"

DST_PATH = r"C:\\Users\\<USERNAME>\\Documents\\DST\\PATH\\"
DST_NAME = "FILENAME_OUTPUT.csv"

#   Read in data. low_memory=False due to mixed data types in large file. 
raw_data = pd.read_csv(SRC_PATH + SRC_NAME, low_memory=False)

#   Set Dealer Name
DEALER_NAME = "DEALER NAME GOES HERE"

#   Filter Out based on conditions
raw_data = raw_data[raw_data["Dealer"] == DEALER_NAME]
raw_data = raw_data[raw_data["Status"] == "Paid"]
raw_data.dropna(subset=["Serial Number"], inplace=True)

#   Write to DST CSV with Dealer Name.
raw_data.to_csv(DST_PATH + DEALER_NAME + DST_NAME, index=False)
