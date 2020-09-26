#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing

# In[2]:


# Data preprocessing is a process to convert raw data into meaningful data using different techniques


# In[3]:


# Why is Data preprocessing important?
    # Data in the real world is dirty
    #   Dirty can be noisy, incomplete, inconsistent and duplicate


# In[18]:


# Machine learning follows the following rule(Learn like kids):-
    # GIGO: Garbage In Garbage Out
# Hence, if your dataset is meaningful your model will respond accurately or else it will not respond accurately


# ## Major steps in Data Preprocessing

# In[19]:


# Major steps in Data Preprocessing:-
    # Data Cleaning
    # Data Integration
    # Data reduction
    # Data Transformation
    # Data Discretization


# In[20]:


# Data Cleaning:- Filling missing values, smooth out noise while identifying outliers(irrelevant data) and
#                 correcting inconsistencies in data


# In[21]:


# Data Integration:- It is a technique to merge data from multiple sources to coherent data store, such as a data warehouse


# In[22]:


# Data Recduction:- It is technique used to reduce data size by aggregating, eliminating redundant features, or clustering
#                   for instance


# In[23]:


# Data Transformation:- Data transormation means data are transformed into forms appropriate for ML model training, such as
#                       normalization, may be applied where data are scaled to fall within a smaller range like 0 to 1
# Data transformation includes:-
    # Aggregation
    # Feature-type conversion
    # Normalization
    # Attribute/feature construction


# In[24]:


# Data Discretization:- Data discretization technique transforms numeric data by mapping values to intervals or concept labels
# It can be used to reduce the number of values for a given continuous attribute by dividing the range of attributes into
# intervals.
# Discretization technique includes:-
    # Binning
    # Histogram Analysis
    # Cluster analysis
    # Decision-tree analysis
    # Correlation analysis
# Ex- Consider a group of people with ages {1,2,3,4,5,6,7,8,9}
#     You can divide them further into sub groups like {1-3,4-6,7-9}...This is discretization


# # Feature Engineering

# In[25]:


# What is Feature Engineering?
    # It is the process to create features/extract features from existing features domain knowledge to increase the performance
    # of the machine learning model


# In[ ]:


# Types of variables:-
    # Numerical Variable:-
        # Discrete variable- Integers
        # Continuous variable- Float
    # Categorical Variable (The values of a categorical variable are selected from a group of categories, also called as labels):-
        # Ordinal Variables (Ordinal variables are categorical variables in which the categories can be meaningfully ordered):-
            # When the ordinal variable convert into number then it has mathematical value
            # Ex:- rating (Good,better,best,bad,worse,worst), grading, months
        # Nominal Variable (It is same like ordinal variable but there is nothing that indicates an intrinsic order of the
        #                   labels and in principle)
            # All labels donot have any order
            # No mathematical value
            # Ex:- Color{red,yellow,blue},products{laptop,bag,books,clothes},language{c,c++,python,c#,js} etc.
    # Date and Time Variables (Contains date only, time only, date and time only variables):-
        # It is found in datasets having info like system ON/OFF, birth report, death report, money withdraw etc
        # Ex:- Date only {Jan-2010}, Time only {10.15 AM}, DateTime {7-Dec-2020 12.00.00}
    # Mixed Variables (Contains both numerical and categorical variables):-
        # Ex:- Percentage {90,80,failed,absent,45}

