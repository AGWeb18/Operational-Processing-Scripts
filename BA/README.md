# RAC AUDIT MACRO

## Efficiently calculate, identify and extract transactions to audit.

## Things to know
* This code is written in VB - run it in Excel
* Ensure you're working with a clean copy. 

## Logic
The mechanics to calculating the number of invoices, choosing random items and enrichment will be explained below. 

### Number of Invoice

The number of invoices to audit is calculated by multiplying the COUNT of invoices by the following rules:
* If the module is SPIFF, STA or IR's and the count of invoice is 1, audit return the count
* If CoI(count of invoice) is >5 but <=500, audit 5 invoices.
* If CoI is >500 but <=1000, audit 10% of the records
* If CoI is >1000 but <= 2000, audit 7.5%
* If CoI is >2000 but <= 5000, audit 5%
* If CoI is >5000, audit 2.5%

#### Code Snippet
```vba
    Range("C6").Formula = "=IF(OR(A6=""Spiffs"",A6=""STA"",A6=""Instant Rebates""),
    IFS(B6<=5,B6,
    AND(B6>5,B6<=500),""5"", 
    AND(B6>500,B6<=1000),B6*0.01,
    AND(B6>1000,B6<=2000), B6*0.0075,   
    AND(B6>2000,B6<5001),B6*0.005,
    B6>=5001,B6*0.0025),
    """")"
```
