import pandas as pd

raw_data = pd.read_csv(r"C:\Users\aridding\Documents\Code Utilities\LargeFIleSplit\971051_74004_DealerClaimsDetails_1.csv", chunksize=100000, low_memory=False)
i = 0
for chunk in raw_data:
    i = i + 1
    chunk.to_csv(r"C:\Users\aridding\Documents\Code Utilities\LargeFIleSplit\ClaimsByDealers_Core_" + str(i) + ".csv")
 
