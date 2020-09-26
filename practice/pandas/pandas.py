#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# # Series

# In[3]:


# Pandas can be used to access series, dataframes and panels.
# Series:- Pandas Series is a one-dimensional labeled array capable of holding data of any type 
# (integer, string, float, python objects, etc.). The axis labels are collectively called index.
# Pandas Series is nothing but a column in an excel sheet.
#################################################################################################
# Dataframe:- Collection of a series is a dataframe
#################################################################################################


# ## To create a series

# In[4]:


# First create a list
list=[1,2,-3,2.4,'sAgaAr',True]


# In[5]:


# To create a series we use the method Series()
series_1=pd.Series(list)
print(series_1)


# In[6]:


# First column has the index for the 2nd column elements


# In[7]:


# Another method to create series...note that both the methods are same
series_2=pd.Series([1,2,3,4,5,5])
print(series_2)


# In[8]:


# To create an empty series
empty_series=pd.Series([])
print(empty_series)


# In[9]:


# We are getting a warning because the datatype of a series is actually object but here it is float64


# In[10]:


# You can change the index to another datatype
series_3=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(series_3)


# In[11]:


# You can change the datatype of the series
series_4=pd.Series([1,2,3,4],index=['a','b','c','d'],dtype=float)
print(series_4)


# In[12]:


# Hence you can remove the above warning by specifying its datatype
empty_series_2=pd.Series([],dtype=float)
print(empty_series_2)


# In[13]:


# You can also add name to the series
series_5=pd.Series([1,2,3,4],name='sagar')
print(series_5)


# In[14]:


# You can create a series for scalar values
series_6=pd.Series(0.5)
print(series_6)


# In[15]:


series_7=pd.Series(0.5,index=[2,3,4])
print(series_7)


# In[16]:


# You can create a series for a dictionary
series_8=pd.Series({'a':1,'b':2})
print(series_8)


# ## Acessing Elements in a series

# In[17]:


# Since series is very much similar to numpy arrays, you can access the values, slice them similar to numpy


# In[18]:


series_1[4]


# In[19]:


series_4['c']


# In[20]:


series_8['a']


# In[21]:


# To slice in a series we can use ":"
series_1[0:4]


# In[22]:


# To get the max value in a series
series_5.max()


# In[23]:


# To get the min value in a series
series_5.min()


# In[24]:


# To print values with a condition within a series we can use conditional operators within the []
series_5[series_5>2]


# ## To perform Mathematical Operations in a series

# In[25]:


series_9=pd.Series([1,2,3,4,5])


# In[26]:


# Adding two series
series_add=series_5+series_9
print(series_add)


# In[27]:


# Since there is a missing value for the index '4'...we got a output 'NaN' which is Not a Number...Similarly you can perform
# all mathematical operations


# # Pandas Dataframe

# In[28]:


#Pandas dataframe is a 2D,size-mutable,potentially heterogenous tabular data structure with labeled axes (rows and columns)


# ## Creating Dataframe

# In[29]:


# To create an empty dataframe
empty_df=pd.DataFrame()
print(empty_df)


# In[30]:


# To create a dataframe you can use a list
list_1=[1,2,3,4,5]
df_1=pd.DataFrame(list_1)
df_1


# In[31]:


# To create a multiple column dataframe you can use list of lists similar of creating an 2D array
list_2=[[1,2,3],[4,5,6],[7,8,9]]
df2=pd.DataFrame(list_2)
df2


# In[32]:


# You can create a dataframe using dictionary where its key will become the column heading
dict1={"sagar":[1,2,3,4],"kumar":[5,6,7,8]}
df3=pd.DataFrame(dict1)
df3


# In[33]:


# Now we will be creating a dataframe with a list of dictionaries
list_dict=[{"a":1,"b":2},{"a":3,"b":4}]
df4=pd.DataFrame(list_dict)
df4


# In[34]:


list_dict=[{"a":1,"b":2},{"a":3,"b":4,"c":5}]
df5=pd.DataFrame(list_dict)
df5


# # Reading CSV files (Comma Seperated Values)

# In[35]:


df6=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv')
df6


# In[36]:


# Note that two '\' is to be used instead of single '\' and the address is to be inserted as a string


# # Writing csv files

# In[37]:


# To get the columns in a dataframe you can use the column method
df6.columns


# In[38]:


# To read n rows of a csv file
df7=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv',nrows=10)
df7


# In[41]:


# To access few of the total columns you can use usecols
df8=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv',nrows=10,usecols=[0,2,4,5])
df8


# In[44]:


#You can use skiprows to skip a number of rows from top
df9=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv',skiprows=2)
df9


# In[45]:


# To skip a particular row with index 'n' you can use skiprows with indeces as a list...ex:- skiprows=[2,4,5]
df10=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv',skiprows=[1,3,5])
df10


# In[48]:


# To change the index of the rows with a column of at dataframe you can use index_col
df11=pd.read_csv('C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv',index_col=1)
df11


# In[ ]:





# In[ ]:




