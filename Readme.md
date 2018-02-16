# 360_LargeInvoice_InputAnalysis

The objective of this code is to calculate the unique number of a specific field in multiple files, stored in a single directory.

## Getting Started

At a high level, this script is directed to a folder in which all the files within it have the same data structure, columns & order.
A hardcoded column - "Invoice number from partner to end-user" - is used to count the number of unique records across all the files dropped in the folder. 


## Prerequisites

To get this script up and running you will need the following programs and python packages installed:

* The latest version of python
* The latest version of pandas




## Installation


### Install Python

[Download the latest version of Python](https://www.python.org/downloads/) 


### Install Pandas


You will need to locate the path to your pip.exe file, from the instance of Python you're currently running (only applies if you have multiple installs of python/anaconda). 


**The path to your pip file is typically in the following location:**
**C:\Users\<username>\AppData\Local\Programs\Python\Python36-32\Scripts**


**If it's not there, here's an automatic way to locate the path to the pip file:**

+ Open CMD - Windows Key + "CMD". Press Enter
+ Enter the following: dir pip.exe /s /p
+ Press Enter
+ Directory of C:\Users\<username>\AppData\Local\Programs\Python\Python36-32\Scripts




###  Validate Installation

+ Open IDLE (or your favourite IDE) by pressing "Windows Key" and typing "IDLE". Press Enter.
+ Type: import pandas as pd
+ Press Enter. 

If no errors appear, you've successfully installed python and pandas. 






### Running the Script

We'll be opening the script, configuring it to your machine and running it. 

1. Open IDLE. 
* Windows Key, "IDLE", Press Enter*

2. Open the script
* CTRL+O, find the .py file.* 

3. On Line 12, the "file_path" variable needs to be pointed to your machine. 
* C:\\Users\ **username** \ Path to the folder with csv's \
