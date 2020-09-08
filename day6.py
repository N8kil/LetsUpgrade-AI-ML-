#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[1]:


str=input()
n=len(str)
a=''
for i in range(n):
    if(str[i]=='@'):
        i=i+1
        while(str[i]!='.'):
            a=a+str[i]
            i=i+1
        else:
            break
print(a)


# # Q2

# In[2]:


l=[]
l=[i for i in input().split(',')]
l.sort()
p = ','.join(i for i in l) 
print(p)


# # sets

# In[3]:


#getting input for sets
s1=set([i for i in input().split(',')])


# In[4]:


for x in s1:
  print(x)


# In[5]:


print("ab" in s1)


# In[6]:


s1.add('1')
print(s1)


# In[7]:


s1.remove('2')
s1


# In[8]:


x = s1.pop()
print(x)


# In[9]:


s1.clear()
s1


# In[10]:


del s1
s1


# In[11]:


s1=set([i for i in input().split(',')])
s2=set([i for i in input().split(',')])


# In[12]:


s3 = s1.union(s2)
s3


# In[13]:


s1.update(s2)
s1


# # Q4

# In[14]:


q=[]
q=[int(i) for i in input()]


# In[15]:


e=q[-1]
x=range(1,e+1)
l=[]
for i in x:
    if i not in q:
        l.append(i)
print(l)


# # Q5

# In[16]:


g=[]
g=[i for i in input()]
g = list(set(g))
g = ','.join(i for i in g) 
print(g)


# In[ ]:




