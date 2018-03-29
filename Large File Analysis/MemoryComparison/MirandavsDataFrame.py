import json
import pandas as pd
import random


#   This dictionary obj will be used for both BYTE and DATAFRAME calculation
#   returns a dictionary object
data = json.load(open(r"C:\Users\ARidding\Desktop\Client Data\Motorola\LargeFileAnalysis\Data\2018_prod-sale-log-store.json\2018_prod-sale-log-store.json"))
#   print(type(data)) - <class 'dict'>

#   seed to set pseudo-random integers
random.seed(180)


#   Of the 400 items sampled, compare a sample of these. (10% to start)
ran_int = [random.randrange(1, 400) for _ in range(0, 40)]


for i in ran_int:
        
    #   returns a unicode object from str()
    obj = str(data['Items'][i])

    #   encode to bytes
    b = obj.encode('utf-8')

    #   read obj (dictionary) into dataframe
    df_obj = pd.DataFrame(data['Items'][i])

    #   Print statements
    #   Note - the 'deep' parameter interrogates for system-level memory consumption
    print("Item number " + str(i) + " is: " + str(len(b)) + " bytes long from json Object")
    print("Item number " + str(i) + " is: " + str(df_obj.memory_usage(deep=True).sum()) + " bytes long from json Object")
    print("="*50)




#   From  the results, it appears there is no correlation between Miranda grouping memory usage and DataFrame memory usage
