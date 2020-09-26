#!/usr/bin/env python
# coding: utf-8

# # Handling Missing Values

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe.csv")
df


# ## isnull() and notnull()

# In[3]:


# Suppose you want a string to be converted to NaN type you can use na_values parameter
df1=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe.csv",na_values="IT sector")
df1


# In[4]:


# You can notice that now IT sector has turned to NaN type...to consider multiple strings of NaN type you can use a list of stings


# In[5]:


# If you want string from a particular column to change to type Nan you can use a disctionary...ex:- na_values={"column1":"string","column2":"string2"}


# In[6]:


# If you are sure that you do not have any missing value, then you can use na_filter=False so that pandas would not filter
# out the missing values and thus the performance of pandas will be improved
df2=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe_not_empty.csv",na_filter=False)
df2


# In[7]:


# To check missing values we can use a method isnull() which returns true if the dataframe has missing values else it returns false
df3=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe.csv",na_values="IT sector")
df3.isnull()


# In[8]:


df4=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe_not_empty.csv")
df4.isnull()


# In[9]:


# To check the number of missing values in each column you can use sum() method since it adds each column and converts False to
# zero and True to one
df3.isnull().sum()


# In[10]:


# To get the total number of missing values in a dataframe, you can sum the values of the above cell,hence
df3.isnull().sum().sum()


# In[11]:


# notnull is opposite of notnull


# In[12]:


# Similarly you can use the above methods to series
import numpy as np
s=pd.Series([1,2,np.nan,4,np.nan])
s


# In[13]:


s.isnull()


# In[14]:


s.isnull().sum()


# ## dropna()

# In[15]:


df5=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\dataframe.csv")
df5


# In[16]:


# dropna is used to drop any row or column containing null values
df5.dropna() #By default its row


# In[17]:


df5.dropna(axis=1) # changing the axis changes the dropna method to drop the row to a column


# In[18]:


# You can use subset parameter in which you mention the column name as a list. If the column contains a null value then it
# drops that row


# In[19]:


df5


# In[20]:


df5.dropna(subset=['Companies'])


# In[21]:


# inplace=True doesnot create a new dataframe (unlike others) but modifies the same dataframe


# ## fillna Method

# In[22]:


# fillna() fills the NaN values with the given values


# In[23]:


df


# In[24]:


df.fillna(7)


# In[25]:


# If you want to fill the name and company col with their respective strings and growth col with numbers, you can use a dictionary
df.fillna({"Companies":"Not Mentioned","Growth":0})


# ## replace method

# In[26]:


# replace method:- Values of the dataframe are replaced with other values dynamically


# In[27]:


df6=df2


# In[28]:


df6


# In[29]:


df6.replace(to_replace="IT sector",value="Finance")


# In[30]:


# to_replace and value can take data types like int, float, string, list, dictionary etc.


# In[31]:


df6.replace(7,100)


# In[32]:


df6.replace([1,2,3,4,5,6,7,8],0)


# In[33]:


df6.replace([1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20])


# In[34]:


df6.replace({"Companies":"IT sector","Growth":"7%"},"NONE")


# In[35]:


# regex identifies user input pattern in the dataframe and replaces them


# In[36]:


df6


# In[37]:


df6.replace(to_replace="[A-Z a-z]",value=0,regex=True)


# In[38]:


# "[A-Z a-z]" means a pattern from A-Z and a-z...Hence, it replaces any string to the value zero


# In[39]:


# To replace a pattern for any particular column we can use dictionary
df6.replace(to_replace={'Companies':'[A-Z a-z]'},value=0,regex=True)


# ## interpolate() Method

# In[40]:


# interpolate method is also used to fill missing values like fillna method but this method guesses the value by understanding a pattern and fills it.


# In[41]:


df7=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Handling Missing Values\\data_2.csv")
df7


# In[42]:


df7.interpolate()


# In[43]:


# Since prediction can be done only on numeric values interpolate method doesnot fill empty string columns


# # Sorting Dataframe

# ## loc[] and iloc[] methods

# In[44]:


# loc[] method access a group of rows or columns by label(s)/index/column name or boolean array


# In[45]:


df6


# In[46]:


df6.loc[0]


# In[47]:


df6.loc[3]


# In[48]:


df6.loc[[0,2,4,6]]


# In[49]:


df6.loc[2:5]


# In[50]:


# If you want to access an index from a column, you can do the following
df6.loc[1,'Companies']


# In[51]:


df6.loc[0:5,"Companies"]


# In[52]:


# You can access values using conditional operators


# In[53]:


df6.loc[df6['Companies']=="IT sector"]


# In[54]:


df6.loc[df6['Expenses']<=6482465]


# In[55]:


df6.loc[df6['Expenses']<=6482465,"Name"]


# In[56]:


df6.loc[df6['Expenses']<=6482465,["Name","Companies"]]


# In[57]:


# iloc method is used for integer location based indexing...df.iloc[rows,columns]
# The difference btw loc and iloc method is that you use col index in iloc and column label in loc


# In[58]:


df6


# In[59]:


df6.iloc[:,0] # All rows and zeroeth column


# In[60]:


df6.iloc[:,1] # All rows and first column


# In[61]:


df6.iloc[[1,2],:]


# In[62]:


df6.iloc[[1,2],[2]] # Rows with index 1,2 and column with index 2


# In[63]:


df6.iloc[0:5,3:5]


# ## groupby() method

# In[64]:


# groupby() method is used to split the data into groups based on some criteria


# In[65]:


df6


# ### To split a dataframe into groups

# In[66]:


grp=df6.groupby(by="Companies")


# In[67]:


grp.groups


# In[68]:


# You can give multiple labels/column names by using a list


# In[69]:


# To visualize the groups you can use a for loop
for i in grp:
    print(i)
    print("-----------------------------------")


# In[70]:


grp1=df6.groupby(by=["Companies","Growth"])


# In[71]:


grp1.groups


# In[72]:


for i,j in grp1:
    print(i)
    print("---------------")
    print(j)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


# In[73]:


print(grp1.groups)


# In[76]:


# You can convert groupby object to a list
list(grp1)


# In[79]:


# You can convert groupby object to a dictionary by first converting it to a list and then dictionary
dict(list(grp1))


# In[80]:


# You can access individual groups by using the method get_group(Parameter by which the dataframe is being grouped)
grp.get_group("IT sector")


# In[83]:


grp1.get_group(("Health","7%"))


# In[86]:


# To get all the statistical parameters you can use describe() method to the dataset...here, we want the statistics of expenses
grp['Expenses'].describe()


# In[89]:


# You can use multiple methods like sum, max, mean etc using aggregate agg() method
grp.agg(["sum","max","min","mean","std"])


# In[91]:


grp["Expenses"].agg(["sum","max","min","mean","std"])


# In[ ]:




