#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv")


# In[3]:


df


# # Read_csv Function part-2

# In[4]:


# You can use haeaders to change the heading to another row...it takes parameter as the index of the row
df1=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv",header=1)
df1


# In[7]:


# If your dataframe doesnot contain any header you can put it to none
df2=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv",skiprows=1,header=None,dtype=object)
df2


# In[9]:


# To add a headers to an empty header dataframe like the one above, you can use perfix whose parameter is a string
df3=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv",skiprows=1,header=None,prefix='Data',dtype=object)
df3


# In[10]:


# Make sure that header is set to none


# In[11]:


# To give names to headings we can use names with parameter as a list of names in string datatype
df4=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv",skiprows=1,names=['a','b','c','d','e','f','g','h','i','j','k','l','m'])
df4


# ## Pandas read_csv function methods

# In[12]:


# Head method is used to print first rows(5 rows) of a dataframe
df.head()


# In[13]:


# You can use parameter for head method print your desired number of rows
df.head(8)


# In[14]:


# Similarly tail method returns bottom 5 rows and returns specified number of rows if a parameter is given
df.tail()


# In[15]:


df.tail(8)


# In[22]:


# To change datatype of a particular column we use dtype parameter where we use dictionary with the key as the column name
# and the value as the datatype
df5=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\Ex_Files_Intro_Data_Science\\Exercise Files\\crime_boston.csv",dtype={"OFFENSE_CODE":"float64","MONTH":"float64"})
df5


# In[ ]:





# In[ ]:




