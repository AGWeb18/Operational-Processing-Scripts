# Weekly Snapshot Report 
The weekly snapshot report converts the "Branch Mapping Report" to a count of DSR's per Sales Manager.
We can use the DSR counts to determine if there's been channel drop off. 

## Getting Started

### 1. Confirm Only 1 File is in the SRC Folder.
- The script will work through ALL files present in the SRC directory
```py
SRC_FILE_PATH = str("C:\\<PATH\\TO\\SRC\\File\\")
```


### 2. Set Up The Source File. 
- Retrieve Branch Mapping Report from email (Randall's report - delivered on Mondays). 
- Delete the first **3 columns** (**Motorola ID,	Motorola Customer Number,	Account Name,**	SalesManager	SR-1, SR-2)
- To confirm, you only want "Sales Manager" and all the columns forward


### 3. Set Up The Py Script.
- Point the paths to the correct directory, for **SRC (source)** and **DST (destination)** files. 
```py
SRC_FILE_PATH = str("C:\\<PATH\\TO\\SRC\\File\\")
DST_FILE_PATH = str("C:\\<PATH\\TO\\DST\\File\\")
DST_FILE_NAME = "OUTPUT_FILENAME.csv"
```

##  Run the Script
- Run the script (F5 in IDLE, CTRL+B in Sublime)
