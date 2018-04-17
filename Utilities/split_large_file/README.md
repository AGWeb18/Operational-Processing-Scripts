### Split Large CSV into Multiple Workbooks - Python
Use this utility to 'break-apart' large CSV's into smaller, more managable files. 

### Getting Started 
1. Change the **SRC_PATH** and **SRC_FILE** to reflect where the Large file is stored.
```py
#   User Defined Paths - placeholder values
SRC_PATH = r"C:\\Users\\<path_to_large_file\\"
SRC_FILE = "LARGE_FILE_GOES_HERE.csv"
```

2. Update the **DST_PATH** and **DST_FILE** to reflect the name/location of the smaller chunks. 
```py
DST_PATH = r"C:\\Users\\aridding\\Documents\\Code Utilities\\LargeFIleSplit\\"
DST_FILE = "FILE_NAME_OUTPUT.csv"
```

3. Ensure that updated files of 100,000 rows is suitable - if  not, update the ```chunksize```
```py
raw_data = pd.read_csv(SRC_PATH + SRC_FILE, chunksize=100000, low_memory=False)
```

4. **Success!**
