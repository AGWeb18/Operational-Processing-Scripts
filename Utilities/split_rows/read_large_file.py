import pandas as pd

#   User Defined Paths - placeholder values
SRC_PATH = r"C:\\Users\\<path_to_large_file\\"
SRC_FILE = "LARGE_FILE_GOES_HERE.csv"
DST_PATH = r"C:\\Users\\aridding\\Documents\\Code Utilities\\LargeFIleSplit\\"
DST_FILE = "FILE_NAME_OUTPUT.csv"


#   Read the large file in via 'chunks' - set to 100k rows. 
raw_data = pd.read_csv(SRC_PATH + SRC_FILE, chunksize=100000, low_memory=False)

#   Value to append to the filename
i = 0

#   For each chunk - write to a new CSV. 
for chunk in raw_data:
    i = i + 1
    chunk.to_csv(\ClaimsByDealers_Core_" + str(i) + ".csv")
 
