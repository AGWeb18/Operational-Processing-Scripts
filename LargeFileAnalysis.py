#   The purpose of this script is to batch process all of the
#   Files in the "file_path" folder
#   From here, a unique count of invoice numbers and the 2 highest invoice counts are returned. 


#   import the required packages
import pandas as pd
import os


#   This file_path would need to be adjusted to work on the users local machine
file_path = str("C:\\Users\\<username>\\Desktop\\Client Data\\Motorola\\Zyme - Data\\RawData\\CleanData\\")

total_unique_invoice_2017 = 0 

#   Create a For loop which works through every file in the folder 
for file_name in os.listdir(file_path):

    #   Read in the data into a DataFrame
    original_data = pd.read_csv(file_path+ file_name, low_memory=False)
                                                                
    #   Remove the unnecessary columns 
    pruned_data = original_data[["Sales Rep contact 18 digit salesforce.com id", "Date of Sale in which Dealer Sales Rep made sale to end-user","Invoice number from partner to end-user"]]

    #   Store the invoice number in a variable
    total_invoice_numbers = pruned_data["Invoice number from partner to end-user"]
    unique_invoice_numbers = total_invoice_numbers.unique()


    print("The File :  " + str(file_name) + "\n" + " The total number of lines in the file is: " + str(len(total_invoice_numbers))+ "\n" +"The total number of unique invoice numbers is: " + str(len(unique_invoice_numbers)))
    print('=' * 50)
    total_unique_invoice_2017 = total_unique_invoice_2017 + len(unique_invoice_numbers)



print("Therefore, the total number of unique invoices in all of 2017 is: " + str(total_unique_invoice_2017))
