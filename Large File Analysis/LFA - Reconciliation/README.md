## Comparing Miranda Byte (character) Length and Dataframe Memory calculation

## Process


###  Data Source
- Extract from MIRANDA db, as a .json object. 


###  Dependancies
- [json package](https://docs.python.org/2/library/json.html)
- [pandas](https://pandas.pydata.org/)
- [random](https://docs.python.org/2/library/random.html)


### High-Level Process
- Load the json object as a dictionary
- Set a seed for reproducibility
- Create a list of random numbers between 0 and 400 (10% sample size). 
- For each random sample, read as unicode and then encode to UTF-8
- Calculate length of object. 
- Compare the length of the Dataframe using the '.memory_usage()' method on the same object. 

 
### Findings
- No correlation between DataFrame memory_usage and byte length.
- Dataframe used significantly less memory
