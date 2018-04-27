#   SCRIPT 3 - By Partner

#   Using the RAW "LAST DATA PULL" - Groupby Method

#   Import the proper packages
import pandas as pd

#   Set up the source file path and name
file_path = r"C:\\Users\\aridding\\Documents\\BA Related\\Monthly\\Monthly Report Development\\"
_name = "Last Raw Data Pull-AR.csv"

#   Read in the raw file - Check for dataset length (data validation)
raw_all_years = pd.read_csv(file_path + _name, low_memory = False, encoding='latin-1', index_col=False)


#   Split the dataset into 2016 and 2018 years
all_years_programs_models_2016 = raw_all_years[raw_all_years["sale.year"] == 2016]
all_years_programs_models_2018 = raw_all_years[raw_all_years["sale.year"] == 2018]


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

#   Percentage Change Calculation
df_merge["Percentage Change"] = (df_merge["2018 Claim Count"]/df_merge["2016 Claim Count"] *100)- 100
df_merge["Percentage Change"] = df_merge["Percentage Change"].round(2)


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

#   Percentage Change Calculation
count_amount_df["Percentage Change - Amount"] = (count_amount_df["2018 Claim Amount"]/count_amount_df["2016 Claim Amount"] *100)- 100
count_amount_df["Percentage Change - Amount"] = count_amount_df["Percentage Change - Amount"].round(2)

#   Sort Values by Claim amount column
count_amount_df = count_amount_df.sort_values(by=["2018 Claim Amount"], ascending=False)
count_amount_df = count_amount_df.round(2)

#   Ranks - 2016 and 2018
count_amount_df["2016 Rank"] = count_amount_df["2016 Claim Amount"].rank(ascending=False)
count_amount_df["2018 Rank"] = count_amount_df["2018 Claim Amount"].rank(ascending=False)


count_amount_df = count_amount_df.iloc[:9, :]
count_amount_df.to_csv(r"C:\Users\aridding\Documents\BA Related\Monthly\Scripts\Reports\partner_march.csv")
