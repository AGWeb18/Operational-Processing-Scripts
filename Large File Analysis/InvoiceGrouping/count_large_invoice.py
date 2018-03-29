#   The purpose of this script is to work through each file.
#   Group based on the 3 fields. 
#   Return the largest invoices per file.
##########################################################################

#   import the required packages
import pandas as pd
import os


#   This file_path would need to be adjusted to work on the users local machine
file_path = str("C:\\Users\\ARidding\\Desktop\\Client Data\\Motorola\\BearComm Only\\DwayneFalcon\\DwayneFalcon - 2017 Analysis\\INPUTFILES\\Zyme_to_360 - CSV\\")


#   Create a For loop which works through every file in the folder - All 2017
for file_name in os.listdir(file_path):
    
    #   Read in the data into a DataFrame
    original_data = pd.read_csv(file_path+ file_name, low_memory=False)

    #   Groupby the 3 fields we aligned on
    grouped_obj = original_data.groupby(["Dealer Customer Number","Sales Rep contact 18 digit salesforce.com id","Invoice number from partner to end-user"])["Row Number"].count()

    try:
        #   if the largest item is larger than 2000 items, review. 
        if int(grouped_obj.nlargest(1)) > 2000:
                print(file_name)
                print(grouped_obj.nlargest(3))
                print("="*50)
        else:
            print(file_name + " doesn't have a grouped invoice, larger than 2,000 lines")
    except:
        #   1 file did not contain any invoice numbers. (Sept26th2017)
        #   This is what caused me to introduce error handling
       print("="*40)
       print("This File " + str(file_name) + " has encountered an error")
       print("="*40)
