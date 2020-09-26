#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([1,2,3])


# In[3]:


a


# In[4]:


print(a)


# In[5]:


b=np.array([[1,2,3],[4,5,6]])


# In[6]:


print(b)


# In[7]:


print(type(a))
print(type(b))


# In[8]:


a.ndim


# In[9]:


b.ndim


# In[10]:


a.size


# In[11]:


b.size


# In[12]:


a.shape


# In[13]:


b.shape


# In[14]:


#To create ones matrix
c=np.ones([5,6],dtype=int)


# In[15]:


c


# In[16]:


#To create a zeroes matrix
d=np.zeros([3,3],dtype=bool)


# In[17]:


d


# In[18]:


d=np.zeros([3,3])


# In[19]:


d


# In[20]:


#To create an empty array
e=np.empty([4,4])
e


# # Creating array with a range

# In[21]:


f=np.arange(1,10,2)  #You can try np.arange(1,10)


# In[22]:


f


# # Linspace

# In[23]:


g=np.linspace(1,10,12)  #It divides the range into 5 equal parts since we are giving a number 5


# In[24]:


g


#  # To convert 1D array into multi-dimensionsal array we use reshape

# In[25]:


h=g.reshape([4,3])
h


# In[26]:


i=g.reshape([2,2,3])
i


# # To convert Multidimensional array to 1D array

# In[27]:


i.ravel()


# # To transpose an array (Interchanging rows and columns)

# In[28]:


b.transpose()


# # Mathematical Operations in Numpy

# In[37]:


x=np.arange(1,7)
y=x.reshape(2,3)
y
m=y.transpose()


# In[38]:


x=np.arange(8,14)
z=x.reshape(2,3)
z


# In[39]:


y+z


# In[40]:


z-y


# In[41]:


z/y


# In[42]:


z*y


# In[43]:


#To perform matrix multiplication
z.dot(m)


# In[45]:


n=z@m
n


# In[47]:


#To check maximum value
n.max()


# In[48]:


#TO check minimum value
n.min()


# In[50]:


#To find the index of the max value
n.argmax()


# In[51]:


#To find the index of the min value
n.argmin()


# In[52]:


#To find min and max of a particular column(axis=0) or row(axis=1) we use axis in max and min function
n.max(axis=0)


# In[53]:


n.min(axis=1)


# In[54]:


#To find the sum of elements in an array
n.sum()


# In[55]:


#To find the sum of elements of a roe or column we use axis in the sum function
n.sum(axis=0)


# In[56]:


#To find the average of elements
n.mean()


# In[57]:


#To find the average of a row or column we use axis
n.mean(axis=1)


# In[59]:


#To find squareroot of the elements
np.sqrt(n)


# In[61]:


#To find the standard deviation
n.std()


# In[63]:


#To find exponents (e^x) of elements
np.exp(n)


# In[65]:


#To find log base e i.e, natural log
np.log(n)


# In[66]:


#To find log base 10
np.log10(n)


# # Python Numpy array slicing (:)

# In[68]:


mx=np.arange(1,101).reshape(10,10)
print(mx)


# In[73]:


#To access individual elements
mx[5][9] # or mx[5,9] 


# In[75]:


#To access complete row
mx[5,:]  # or mx[5].....  ':' means to access complete row or column


# In[76]:


#To access complete column
mx[:,5]


# In[81]:


#Note that the above is an 1D array...To convert this into 2D array we can use the slice operator ":" mentioning 'x:y' which
# means from x row/column to y-1 row/column
mx[:,5:6]
# The above command means you wanted every row and the column with index 5...Now you can observe that you got an 2D array


# In[83]:


# To access few rows with few of their columns
mx[1:4,1:4] #We are accessing 2,3 and 4 rows with 2,3 and 4 columns...remember that indeces of array starts with zero


# In[85]:


#To access all rows with few of their columns
mx[:,2:5]


# In[86]:


#To check the size of an individual element in an array
mx.itemsize


# In[87]:


mx.dtype


# # Python Numpy array Concatenation and Split

# In[89]:


arr1=np.arange(1,17).reshape(4,4)
arr1


# In[90]:


arr2=np.arange(17,33).reshape(4,4)
arr2


# In[91]:


#To concatenate two arrays
arr_concatenated=np.concatenate((arr1,arr2)) #This is column-wise concatenation
arr_concatenated


# In[92]:


#To perform row-wise concatenation
np.concatenate((arr1,arr2),axis=1)


# In[93]:


#To split an array we use split function
np.split(arr1,2) #here we split the array into 2 sections


# In[98]:


#To split an array row-wise
arr3=np.split(arr1,2,axis=1)


# In[99]:


#Split function splits the array into a list which stores the array
type(arr3)


# In[100]:


type(arr3[0])


# In[102]:


#To use split function using indeces and not sections
arr4=np.array([11,12,13,14,15,16,17,18,19])
np.split(arr4,[4,7])


# # To find trigonometric functions sin,cos and tan in numpy

# In[103]:


import matplotlib.pyplot as plt


# In[110]:


#To find the values in degrees...note that in degrees and not in radians
np.sin(90)


# In[105]:


np.sin(180)


# In[106]:


#The above are the accurate floating values


# In[107]:


np.cos(0)


# In[108]:


np.cos(180)


# In[136]:


#To convert degrees to radians
np.cos(np.deg2rad(180))


# In[137]:


np.tan(np.deg2rad(90))


# In[138]:


#To visualize trigonometric graphs


# In[139]:


#Sin graph
x_values=np.arange(0,3*np.pi,0.1)
x_values


# In[154]:


y_values_sin=np.sin(x_values)
y_values_sin


# In[155]:


plt.plot(x_values,y_values_sin)
plt.show()


# In[156]:


#Cos graph
y_values_cos=np.cos(x_values)
plt.plot(x_values,y_values_cos)
plt.show()


# In[157]:


#Tan graph
y_values_tan=np.tan(x_values)
plt.scatter(x_values,y_values_tan,5)
plt.show()


# # Random Sampling in Numpy

# In[158]:


import random


# In[172]:


#Generating random values
random.random() #Generates a number between 0 and 1


# In[164]:


#Generating random values between a range
random.randrange(1,100)


# In[169]:


#To create a random value in a array
np.random.random(1) # size of the array is one


# In[170]:


np.random.random(5)


# In[173]:


np.random.random([3,3])


# In[174]:


np.random.randint(1,10)


# In[175]:


#The above code is not giving an array since shape of the array is not defined
np.random.randint(1,10,[5,5])


# In[176]:


np.random.randint(1,10,[2,5,5])


# In[180]:


# You can notice that random function is generating random values on every refresh...but you want to have same random values on
# every refresh, then you can use seed function with a number as a parameter which will act as a tag
np.random.seed(5)
np.random.randint(1,5,[2,3,3])


# In[183]:


np.random.seed(5)
np.random.randint(1,5,[2,3,3])


# In[179]:


# You will observe that the above two cells have the same output


# In[184]:


#You can also get random values using rand function
np.random.rand(4)


# In[185]:


np.random.rand(4,2)


# In[186]:


#To get both positive and negative values you can use randn function
np.random.randn(3,3)


# In[187]:


#To get random values from a list we use choice function
list=[11,12,13,14,15]
np.random.choice(list)


# In[189]:


for i in range(1,11):
    print(np.random.choice(list))


# In[191]:


# To change the permutation of a list we can use permutation function
np.random.permutation(list)


# In[192]:


for i in range(120):
    print(np.random.permutation(list))


# # String operation,comparision and information

# In[194]:


first_name="Sagar"
last_name=" Kumar"


# In[196]:


first_name+last_name #String concatenation


# In[198]:


np.char.add(first_name,last_name) #To concatenate strings in an array


# In[199]:


#To convert characters to lower case
np.char.lower(first_name)


# In[201]:


#To convert the characters into upper case
np.char.upper(last_name)


# In[202]:


#To center a string we use center method 
np.char.center(first_name,30) #Size of the string is 30


# In[203]:


np.char.center(first_name,30,fillchar="*")


# In[204]:


#To split a sentence into words
sentence="Hello World, hello"


# In[205]:


np.char.split(sentence)


# In[208]:


sentence.split(" ") #Note that this is a list and the above is an array due to numpy


# In[209]:


#To split between lines we use splitlines method
lines="Hello world\nHello world"


# In[210]:


np.char.splitlines(lines)


# In[211]:


#We can use join method to join a character in between a string


# In[212]:


np.char.join("/",first_name)


# In[213]:


np.char.join([":","/"],[first_name,last_name])


# In[214]:


#We can use replace method to replace words
np.char.replace(first_name,"a","A")


# In[215]:


#To compare strings we use equal method


# In[216]:


np.char.equal(first_name,last_name)


# In[218]:


np.char.equal(first_name,first_name)


# In[219]:


# To count no. of times a character or a word repeats we use count method


# In[220]:


np.char.count(first_name,"a")


# In[223]:


np.char.count(lines,"Hello")


# In[224]:


# TO find a character or a word we use find method... it returns the index of the character


# In[225]:


np.char.find(first_name,"a")


# In[228]:


np.char.find(lines,"world")


# In[ ]:




