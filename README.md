# python-functions
Creating a reusable functions in python

#EDA:

#### EDA function is a redundant day to day analysis we do when ever we get data. So I thought these functions can reduce the redundancy of EDA process. There are list of functions that we use. PFB the functions

## null_values 
  ### parameters : dataframe, values(default to "remove"), column(default to None)
    #### dataframe: dataframe on which function has to perform it's operation
    #### value : Here we are allowed to pass 3 parameters
    ##### If we select "remove", the function removes entire NA values in dataframe
    ##### If we pass "count" it just returns count of NA values in each column of dataframe
    ##### If we pass "remove_for_column" we need pass optional parameter "column" where when we specify column remove rows that are NA only in that column

## pop_column
  ### parameters: dataframe, column(default to None)
    #### dataframe: dataframe on which function has to perform it's operation
    #### column: we can pass this parameter either a single column in a string or a list of columns. The function will remove those columns and will return the resultant dataframe back after removing those columns
    
## numeric_column_distribution
  ### parameters: dataframe
        #### dataframe: dataframe on which function has to perform it's operation
        #### this function returns hist distribution plots for all numeric columns
        
## count_plot
  ### parameters: dataframe
        #### dataframe: dataframe on which function has to perform it's operation
        #### this function returns count frequnecies for all object type columns
        
## corr
  ### parameters: dataframe
        #### dataframe: dataframe on which function has to perform it's operation
        #### this function gives the correlation plot for the dataframe
        
## box_plot
  ### parameters: dataframe, column(default to None) 
        #### dataframe: dataframe on which function has to perform it's operation
        #### column : When column is passed it gives box plot only to that column else to entire dataframe
        
##### I have attcahed a sample .ipynb file using these functions. You can use them as reference for these
        
        
  
