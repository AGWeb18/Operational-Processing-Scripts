#   GENERATE A Q1 CLR Report
#   Retreive the following data points

#       Data Points
################################
#   # of transactions received
#   # of lines processed
#   # of transactions approved
#   # of lines rejected
#   # of lines declined
#   # approved - base
#   # approved - mo
#   # approved - mr
#   # approved - csl
#   # approved - promo
#   # of unique sales reps
#   # of unique dealers
#   # of unique models
################################

#   Import required packages
import pandas as pd
import os

#   SET SRC and DST locations
SRC_file = r"C:\Users\aridding\Documents\\BA Related\Reporting\Q1 - CLR Report\raw_data_allCLR's_q12018_v2.txt"

SRC_folder = r"C:\\Users\\aridding\\Documents\\BA Related\\Reporting\\Q1 - CLR Report\\Q1_processed\\"

DST_file = r"C:\Users\aridding\Documents\\BA Related\Reporting\Q1 - CLR Report\Q12018_CLR_Report_04302018.csv"


#   Create dummy variables
transactions_received = 0
transactions_approved = 0
lines_processed = 0
lines_rejected = 0
lines_declined = 0
approved_base = 0 
approved_mo = 0
approved_mr = 0
approved_csl = 0
approved_promo = 0 
unique_contact_id = 0 
unique_dealers = 0
unique_models = 0

with open(SRC_file, 'r') as f:
#   Count the unique # of master_line_id's from the POS_ZYME location.
#   Count the unique # of SA - Dealer - Model
    raw_chunk = pd.read_csv(f, sep='\t', chunksize=1000000)
    for chunk in raw_chunk:
        transactions_received = transactions_received + (int(len(chunk['master_line_id'].unique())))
        unique_contact_id = unique_contact_id + (int(len(chunk['sales_rep_contact_id'].unique())))
        unique_dealers = unique_dealers + (int(len(chunk['dealer_name'].unique())))
        unique_models = unique_models + (int(len(chunk['model_number_or_sku'].unique())))
        

#   Instantiate empty lists - one for each status reason
master_id_accounted_rejected = []
master_id_accounted_approved = []
master_id_accounted_declined = []
master_id_accounted_submitted = []

#   Empty list for programs
master_id_programs_approved = []

#   Empty DF for program
approved_program_value_counts = pd.DataFrame()

#   For each file in the specified folder....
for file_name in os.listdir(SRC_folder):
    with open(SRC_folder + file_name, 'r') as big_f:
        print("Processing the following: " + str(file_name))

        #   Loop through file - chunk by chunk - append to appropriate list
        raw_chunk_status = pd.read_table(big_f, sep='\t', chunksize=100000, low_memory=False)
        for chunk in raw_chunk_status:


            #   Pull Data based on Status
            chunk_rejected = chunk[chunk['status'] == "Rejected"]
            chunk_approved = chunk[chunk['status'] == "Approved"]
            chunk_declined = chunk[chunk['status'] == "Declined"]
            chunk_submitted = chunk[chunk['status'] == "Submitted"]

            #   Append to appropriate lists
            master_id_accounted_rejected.append(chunk_rejected['master_line_id'])
            master_id_accounted_approved.append(chunk_approved['master_line_id'])
            master_id_accounted_declined.append(chunk_declined['master_line_id'])
            master_id_accounted_submitted.append(chunk_submitted['master_line_id'])
            
            #   Extract program data
            #   Prune the dataset to the 2 columns
            approved_chunk = chunk_approved[['master_line_id', "program_name"]]
            approved_program_count_df = pd.DataFrame(approved_chunk)
       
            approved_program_value_counts = approved_program_value_counts.append(approved_program_count_df, ignore_index=True)

approved_program_value_counts = approved_program_value_counts.drop_duplicates(subset='master_line_id')


#   Flatten nested lists
accounted_rejected = [item for sublist in master_id_accounted_rejected for item in sublist]
accounted_approved = [item for sublist in master_id_accounted_approved for item in sublist]
accounted_declined = [item for sublist in master_id_accounted_declined for item in sublist]
accounted_submitted = [item for sublist in master_id_accounted_submitted for item in sublist]

#   Determine program count
#   approved - base
#   approved - mo
#   approved - mr
#   approved - csl
#   approved - promo

#   Approved value_counts



#   Calculate the required metrics. 
transactions_approved = int(len(accounted_approved))
lines_rejected = int(len(accounted_rejected))
lines_declined = int(len(accounted_declined))
lines_submmited = int(len(accounted_submitted))
lines_processed = lines_rejected + lines_declined + lines_submmited + transactions_approved

#   Print the data in a user-friendly manner.
print("Q1 - CLR Report Findings...")
print("="*50)
print("The number of transactions received is: " + str(transactions_received))
print("The number of lines processed is: " + str(lines_processed))
print("The number of lines approved is: " + str(transactions_approved))
print("The number of lines rejected is: " + str(lines_rejected))
print("The number of lines declined is: " + str(lines_declined))
print("The number of lines submitted/On-Hold is: " + str(lines_submmited))

#   The unique Model/SA/Dealer information
print("The number of unique Sales Associates is: " + str(unique_contact_id))
print("The number of unique Dealers is: " + str(unique_dealers))
print("The number of unique Models is: " + str(unique_models))


