#  Extract Clean Data
Test/Extract line items for success criteria and document those with errors. 

### Getting Started
- Use this script to batch process multiple files in a folder, where there are errors in some files.  
- If the row of the file does not meet the success criteria (defined below), then store in a separate worksheet. 


### Success Criteria
- Count of Columns must equal 42. This is the correctly parsed number of columns per row. 
- The 'status' column must contain 1 of the allowable values. This captures the edge case of a correct number of columns (potentially hidden), with improper data. (Approved, Submitted, Declined, On Hold, Paid, Deleted are the allowable values). 

### Improvements - Next steps
To improve the efficiency of the script, it would be valuable to vectorize the operation.
- Where the column 'status' is not one of the allowable values, inset "NA". 
- Where the column 'status' is not NA, export to a CSV. If 'status' is "NA", export to distinct CSV. 
