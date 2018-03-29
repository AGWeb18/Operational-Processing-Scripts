#  Group Invoice - Analysis
Read all invoices from 2017, Group them and rank the count. Assess whether these have made it to Core. 

### Getting Started ###
All you need to get started is *Python* and *pandas* to get started
 
### Prerequisites
We'll be using pandas 'groupby' method here for heirarchial grouping 
```python
import pandas as pd
```

### Installing the Script
 - Dowload the .py script
 - Ensure the userpaths are correct
 ```python
 file_path = str("C:\\Users\\<username>\\Desktop\\<FILE_PATH_GOES_HERE>")
 ```

- Ensure the fields being referenced are the correct fields. 
```python
grouped_obj = original_data.groupby(["Dealer Customer Number","Sales Rep contact 18 digit salesforce.com id","Invoice number from partner to end-user"])["Row Number"].count()
```


### Setup of Directory
 - Create a folder
 - Store all files (CSV) you want to be searched/analyzed. 
 - Threshold of 2,000 items is currently set - reassess. 
 ```python
 if int(grouped_obj.nlargest(1)) > 2000:
 ```
