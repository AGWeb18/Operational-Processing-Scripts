#   Using the RAW "LAST DATA PULL" - Groupby Method

#   Import the proper packages
import pandas as pd


#   Set up the source file path and name
file_path = (r"C:\Users\aridding\Documents\BA Related\Reporting\Monthly\Monthly Report Development\April\Last Raw Data Pull3.csv")

chunks = []

raw_all_years = pd.read_csv(file_path, low_memory=False, encoding='latin-1', index_col=False, chunksize=250000)

#   Read in the raw file - Check for dataset length (data validation)
for chunk in raw_all_years:

	chunks.append(chunk)



massive_dataset = pd.concat(chunks, axis=0)

#   Split the dataset into 2016 and 2018 years
all_years_programs_models_2016 = massive_dataset[massive_dataset["sale.year"] == 2016]
all_years_programs_models_2018 = massive_dataset[massive_dataset["sale.year"] == 2018]



#   Print descriptions - COUNT IS NOT ACCURATE FOR 2018 - SUM QUANTITY
claim_count_2018 = all_years_programs_models_2018.groupby(["dealer"])["quantity"].sum()
claim_count_2016 = all_years_programs_models_2016.groupby(["dealer"])["quantity"].sum()


#   Claim Count - Breakdown by program - DataFrame. 
df_claim_count_2016 = pd.DataFrame(claim_count_2016)
df_claim_count_2018 = pd.DataFrame(claim_count_2018)


#   Merge the dataframes to compare across years
df_merge = pd.concat([df_claim_count_2016, df_claim_count_2018], axis=1)

#   Rename the columns to be able to divide properly
df_merge.columns = ["2016 Claim Count", "2018 Claim Count"]


#   Print descriptions - COUNT IS NOT ACCURATE FOR 2018 - SUM QUANTITY
claim_amount_2018 = all_years_programs_models_2018.groupby(["dealer"])["claim.amount"].sum()
claim_amount_2016 = all_years_programs_models_2016.groupby(["dealer"])["claim.amount"].sum()


#   Claim Count - Breakdown by program - DataFrame. 
df_claim_amount_2016 = pd.DataFrame(claim_amount_2016)
df_claim_amount_2018 = pd.DataFrame(claim_amount_2018)


#   Merge the dataframes to compare across years
df_merge_amount = pd.concat([df_claim_amount_2016, df_claim_amount_2018], axis=1)

#   Rename the columns to be able to divide properly
df_merge_amount.columns = ["2016 Claim Amount", "2018 Claim Amount"]

#   Merge the Count and Amount DFs
count_amount_df = pd.concat([df_merge, df_merge_amount], 1)



#   Ranks - 2016 and 2018
count_amount_df["2016 Rank"] = count_amount_df["2016 Claim Amount"].rank(ascending=False)
count_amount_df["2018 Rank"] = count_amount_df["2018 Claim Amount"].rank(ascending=False)




#   Percentage Change Calculation
count_amount_df["Percentage Change - Count"] = (count_amount_df["2018 Claim Count"]/count_amount_df["2016 Claim Count"] *100)- 100
count_amount_df["Percentage Change - Count"] = count_amount_df["Percentage Change - Count"].round(2)




##   Percentage Change Calculation
count_amount_df["Percentage Change - Amount"] = (count_amount_df["2018 Claim Amount"]/count_amount_df["2016 Claim Amount"] *100)- 100
count_amount_df["Percentage Change - Amount"] = count_amount_df["Percentage Change - Amount"].round(2)
count_amount_df = count_amount_df.round(2)


count_amount_df = count_amount_df.sort_values('2018 Claim Amount', ascending=False)
count_amount_df = count_amount_df.iloc[:9,:]

##   Append the rows of the DataFrame to your worksheet
count_amount_df.to_csv(r"C:\Users\aridding\Documents\BA Related\Reporting\Monthly\Monthly Report Development\April\Output\partner_april.csv")#

