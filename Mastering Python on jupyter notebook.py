#!/usr/bin/env python
# coding: utf-8

# Mastering Python ZerotoHero
# 

# This is the beginning of learning

# In[1]:


print("hello world")


# In[2]:


a = b + c


# In[3]:


b = 5


# In[4]:


c = 7


# In[5]:


a = b + c


# In[7]:


print('a = b + c')


# # Bool

# In[8]:


a = True
b = True
c = False


# In[9]:


get_ipython().run_line_magic('whos', '')


# In[10]:


print(a and b)
print(a and c)
print(c and a)


# In[11]:


d = a or c
print(d)


# In[12]:


not (a)


# In[13]:


not (b)


# In[14]:


t = not(c)


# In[15]:


type(t)


# In[16]:


print(t)


# In[17]:


not((a and b) or (c and d))


# # comparisms

# In[18]:


print(2<3)


# In[19]:


c = 2<3
print(type(c))
print(c)


# In[20]:


d = 3==4


# In[21]:


print(d)


# In[22]:


3==3.0


# In[23]:


x = 4
y = 9
z = 8.3
r = -3


# In[24]:


get_ipython().run_line_magic('whos', '')


# In[25]:


(x<y) and (z<y) or (r==x)


# In[26]:


(r==x) and (x<y) or (z>y)


# In[27]:


False or False and True


# In[28]:


True or True or False


# In[29]:


2!=3


# In[30]:


print((not(2!=3) and True) or (False and True))


# In[32]:


print(round(4.5578))


# In[33]:


print(round(4.3214))


# In[34]:


print(round(4.56789,2))


# In[35]:


divmod (22 , 10)


# In[37]:


G = divmod (34 , 10)


# In[38]:


print(G)


# In[39]:


G[0]


# In[40]:


G[1]


# In[41]:


print(type(G))


# In[42]:


34//9


# In[43]:


34%9


# In[44]:


isinstance(3, int)


# In[46]:


isinstance(4.5, int)


# In[47]:


isinstance(4.5,(int,float,str))


# In[49]:


isinstance(2+5j,(int, float, str, complex))


# In[50]:


4**6


# In[51]:


y = 4**6


# In[52]:


print(y)


# In[53]:


pow(4,6,3)


# In[ ]:




