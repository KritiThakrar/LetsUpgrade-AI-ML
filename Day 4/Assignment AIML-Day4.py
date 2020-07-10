#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question 1
a=complex(input("Enter the first numer: "))
b=complex(input("Enter the second numer: "))
add=a+b
sub=a-b
multiply=a*b
divide=a/b
print("Addition = ",add)
print("Substraction = ",sub)
print("Division = ",divide)
print("Multiplication = ",multiply) 


# #Quetion 2
# range() function is used to generate numbers from given starting integer to end integer.It is used in for loop.

# It parameters are start,stop and step.

# Start is the lower limit,Stop is the upperlimit and it displays till the range less then the given integer. and step is the differnce between the given integer.

# In[2]:


for i in range(3):
    print(i,end=',')


# In[4]:


for j in range(4,8):
    print(j,end=',')


# In[6]:


for k in range(0,10,2):
    print(k,end=',')


# In[2]:


#Question 3
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
sub=a-b
if (sub>25):
    print("Multiplication=",(a*b))
else:
    print("Division= ",(a//b))


# In[6]:


#Question 5
for i in range(12,22):
    if(i%2==0):
        print("Square of the number ",(i**2),"minus 2 is ",(i**2-(2)))


# In[16]:


#Question 5
for i in range(1,10):
    if(i%2==0 and i>7):
        print(i)


# In[ ]:




