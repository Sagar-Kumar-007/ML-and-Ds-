#!/usr/bin/env python
# coding: utf-8

# # Line plot

# In[1]:


import matplotlib.pyplot as plt


# In[10]:


days=[1,2,3,4,5,6,7,8]
temp=[36,36.5,37,38,38.5,39,42,43]


# In[12]:


# To draw a line plot you can use plot(x-axis,y-axis) method
plt.plot(days,temp)
plt.title("Days vs Temperature")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.show()


# In[14]:


# You can adjust the xmin,xmax,ymin and ymax values by using axis() method
plt.plot(days,temp)
plt.title("Days vs Temperature")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.axis([0,8,0,44])
plt.show()


# In[27]:


# To change the color of the graph,line styles,line width and put marker
plt.plot(days,temp,color="r",marker="o",linestyle=":",linewidth=3)
plt.title("Days vs Temperature",fontsize=15)
plt.xlabel("Days",fontsize=13)
plt.ylabel("Temp",fontsize=13)
plt.legend(["days vs temp"],loc=4) #loc represents location of the legend...4 represents bottom-right corner
plt.show()


# In[29]:


# If you are drawing multiple graphs...then you can set label in the plot method to create a legend
# To change the color of the graph,line styles,line width and put marker
plt.plot(days,temp,color="r",marker="o",linestyle=":",linewidth=3,label="days vs temp")
plt.title("Days vs Temperature",fontsize=15)
plt.xlabel("Days",fontsize=13)
plt.ylabel("Temp",fontsize=13)
plt.legend(loc=4) #loc represents location of the legend...4 represents bottom-right corner
plt.show()


# In[33]:


# To draw grid you can import style from matplotlib and use the method use()


# In[34]:


from matplotlib import style


# In[38]:


plt.plot(days,temp,color="r",marker="o",linestyle=":",linewidth=3,label="days vs temp")
style.use('ggplot')
plt.title("Days vs Temperature",fontsize=15)
plt.xlabel("Days",fontsize=13)
plt.ylabel("Temp",fontsize=13)
plt.legend(loc=4)
plt.show()


# In[39]:


# List of style names
style.available


# In[41]:


# To draw multiple plots in a single graph you can:-
mumbai_temp=[34,32,35,38,33,38,34,35]
plt.plot(days,temp,color="r",marker="o",linestyle=":",linewidth=3,label="Delhi Temp")
plt.plot(days,mumbai_temp,color="g",marker="o",linestyle=":",linewidth=3,label="Mumbai Temp")
plt.title("Days vs Temperature",fontsize=15)
plt.xlabel("Days",fontsize=13)
plt.ylabel("Temp",fontsize=13)
plt.legend(loc=4)
plt.show()


# # Histograms

# In[45]:


import numpy as np
import random


# In[46]:


# Histogram plots a graph btw a category and number of times that category is repeated


# In[50]:


students_age_1=np.random.randint(18,45,size=100)
students_age_1


# In[51]:


students_age_2=np.random.randint(15,40,size=100)
students_age_2


# In[56]:


# To draw a histogram, you can use a method called hist()
style.use("default")
plt.hist(students_age_1)
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.show()


# In[58]:


# To adjust the x-axis range you can use the bins parameter of hist() method
plt.hist(students_age_1,bins=[15,20,25,30,35,40,45])
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.show()


# In[59]:


# To adjust the width of the bar you can use rwidth
style.use("default")
plt.hist(students_age_1,bins=[15,20,25,30,35,40,45],rwidth=0.8)
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.show()


# In[66]:


# To show different histograms in a single graph
plt.hist(students_age_1,bins=[15,20,25,30,35,40,45],rwidth=0.4,label="students_1")
plt.hist(students_age_2,bins=[15,20,25,30,35,40,45],rwidth=0.4,color="r",label="students_2")
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.legend()
plt.show()


# In[67]:


# You can notice that the graph is not visualized properly...to rectify this we can use hist() method only once with two parameters
plt.hist([students_age_1,students_age_2],bins=[15,20,25,30,35,40,45],color=["r","b"],rwidth=0.8,label=["students_1","students_2"])
#plt.hist(students_age_2,bins=[15,20,25,30,35,40,45],rwidth=0.4,color="r",label="students_2")
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.legend()
plt.show()


# In[69]:


# To change the size of the histogram you can use figure parameter
plt.figure(figsize=(16,9))
plt.hist([students_age_1,students_age_2],bins=[15,20,25,30,35,40,45],color=["r","b"],rwidth=0.8,label=["students_1","students_2"])
plt.title("Student Age Category")
plt.xlabel("Student's Age")
plt.ylabel("No. of students")
plt.legend()
plt.show()


# # Bar chart

# In[70]:


classes=["Python","R","AI","ML","DS"]
class1=[30,10,20,25,10]
class2=[40,5,20,20,10]
class3=[35,5,30,15,15]


# In[71]:


# You can draw a bar chart using bar() method and to draw horizontal bar chart you can use barh() method


# In[72]:


plt.bar(classes,class1)


# In[73]:


plt.barh(classes,class2)


# In[74]:


# Other parameters are similar to previous charts and to know more about parameters type the method and then press shift+tab


# In[75]:


# To draw multiple barcharts in a single graph, you can:-
plt.bar(classes,class1,color="r")
plt.bar(classes,class2,color="b")
plt.bar(classes,class3,color="g")
plt.show()


# In[76]:


# Since these are overlapping, you can adjust their width such that they dont ovelap


# In[86]:


width=0.2;
classes_index=np.arange(len(classes))
plt.bar(classes_index,class1,color="r",width=width,label="Class-1")
plt.bar(classes_index+width,class2,color="b",width=width,label="Class-2")
plt.bar(classes_index+2*width,class3,color="g",width=width,label="Class-3")
plt.legend()
plt.show()


# In[90]:


# But you can see that the above graph doesnot show x-axis labels...to rectify this you can use xticks() method
width=0.2;
classes_index=np.arange(len(classes))
plt.bar(classes_index,class1,color="r",width=width,label="Class-1")
plt.bar(classes_index+width,class2,color="b",width=width,label="Class-2")
plt.bar(classes_index+2*width,class3,color="g",width=width,label="Class-3")
plt.xticks(classes_index+width,classes,rotation=0)
plt.legend()
plt.show()


# # Scatter plot

# In[91]:


# To draw scatterplot you can use scatter() method


# In[93]:


import pandas as pd


# In[98]:


df=pd.read_csv("C:\\Users\\91830\\Downloads\\data science\\practice\\Matplotlib\\googleplaystore.csv",nrows=1000)
df


# In[99]:


df.shape


# In[103]:


x=df["Rating"]
y=df["Reviews"]


# In[106]:


plt.scatter(x,y)
plt.show()


# In[107]:


# The parameters are similar to the other graphs


# In[121]:


# To draw multiple scatter plots in a single graph, you can:-
plt.scatter(x,y,label="Reviews",alpha=0.5)
plt.scatter(x,df["Installs"],label="Installs",alpha=0.5)
plt.axis(ymin=0)
plt.legend()
plt.show()


# In[ ]:




