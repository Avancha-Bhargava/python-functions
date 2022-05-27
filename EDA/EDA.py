#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('bmh')


# In[18]:


# This is for checking null values in the dataframe, 
#values can be given either remove or count where remove typically returns dataframe without null values, 
# count will give NA for each column
# remove_for_column when passed with column name will remove rows having NA in that column


# In[19]:


def null_values(df, values="remove", column= None):
    if (values == "remove"):
        return df.dropna()
    elif (values == "count"):
        return df.isna().sum()
    elif (values== "remove_for_column"):
        return df[df[column].notna()]
    else:
        print("Not an valid Option")
        return 0

    


# In[20]:


# Removing user defined columns.


# In[21]:


def pop_column(df,column=None):
    if (type(column) is str):
        if (column):
            df.pop(column)
            return df
        else:
            print("Not a valid column name")
            return df
    elif (type(column) is list):
        if (column):
            [df.pop(x) for x in column]
            return df
        else:
            print("Not a valid column name")
            return df
        


# In[22]:


# gives hist plots for numerical columns


# In[28]:


def numeric_column_distribution(df,columns = None):
    df= df.select_dtypes(include = ['float64', 'int64'])
    return df.hist(figsize=(df.shape[0]*2, df.shape[1]*2), bins=50, xlabelsize=8, ylabelsize=8)


# In[29]:


# this is a frequency plot for categorical variables


# In[30]:


def count_plot(df):
    df = df.select_dtypes(include = ['O'])
    if(df.shape[1]>3):
        shape= 3
    else:
        shape = df.shape[1]
    
    fig, axes = plt.subplots(round(df.shape[1] / 3), shape, figsize=(df.shape[0]*2, df.shape[1]*2))
    for i, ax in enumerate(fig.axes):
        if i < len(df.columns):
            sns.countplot(x=df.columns[i], alpha=0.7, data=df, ax=ax)
    fig.tight_layout()


# In[31]:


# getting a correlation matrix


# In[32]:


def corr(df):
    return df.corr(method='pearson', min_periods=1).style.background_gradient(cmap='coolwarm')


# In[33]:


# for getting a boxplot
# We can pass entire dataframe where it returns boxplots for entire dataframe or just pass a column it return box plot for that column


# In[34]:


def box_plot(df,column=None):
    df = df.select_dtypes(include = ['float64', 'int64'])
    if(column):
        df = pd.DataFrame(df[column])
    sns.boxplot(x="variable", y="value", data=pd.melt(df))
    return plt.show()


# In[ ]:





# In[ ]:




