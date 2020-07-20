#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question 1
print(input().split("@")[1].split(".")[0])


# In[30]:


#Question 2
l=input("Enter comma seperated sequences of words ")
l=l.split(",")
l=sorted(l)
print(",".join(l))


# #Question 3
#  Set
#  
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# 

# In[1]:


s = {"apple", "banana", "cherry"}
print(s)


# In[20]:


s = {"apple", "banana", "cherry"}
print("banana" in s)
s.add("Papaya")
print(s)
s.update(["Pineapple","orange","Kiwi"])
print(s)
print(len(s))
s.remove("Pineapple")
print(s)
s.pop()
print(s)
s.clear()
print(s)


# In[22]:


s1={1,3,5,7,9}
s2={2,4,6,8,10}
s3=s2.union(s1)
print(s3)
s1.update(s2)
print(s1)


# In[28]:


s1={1,2,3,4,5,6,7,8,9,10}
s2={2,4,6,8,10}
s4=s2.intersection(s1)
print(s4)
s2.issubset(s1)


# In[56]:


#Question 4
def getmissingno(a): 
    n = len(a) 
    total = (n + 1)*(n + 2)//2
    s = sum(a)
    return total - s 
a=list(map(int,input().split()))
m = getmissingno(a)
print(m)


# In[ ]:


#Question 5
fl = []
dup = list(map(int,input().split()))
for n in dup: 
    if n not in fl: 
        fl.append(n) 
print(fl)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




