#!/usr/bin/env python
# coding: utf-8

# # Data Frame

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
df


# In[5]:


print(df.loc[0:3,'A'])


# In[8]:


print(df.loc[:4,:])


# In[13]:


print(df.iloc[:,0])


# In[17]:


print(df.iloc[0:2,1:3])


# In[18]:


print(df.iloc[:,-1])


# In[21]:


print(df.iloc[:,-2:-1])


# # Python Visualization

# In[28]:


df=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
df
df.plot.bar()


# In[29]:


df.plot.bar(stacked=True)


# In[30]:


df.plot.barh(stacked=True)


# In[34]:


df.plot.hist()


# In[36]:


df.plot.hist(stacked=True)


# In[37]:


df.plot.box()


# In[39]:


df.plot.area()


# In[41]:


df=pd.DataFrame(np.random.rand(50,4),columns=['A','B','C','D'])
df.plot.scatter(x='A', y='B')


# Change the index

# In[47]:


import pandas as pd


# In[57]:



df= pd.DataFrame({"Day" :[1,2,3,4], "Visitiors":[100,200,300,400], "Bounce_Rate":[209,423,123,346]})
print(df)


df1=df.set_index("Day")
df1


# In[58]:


df.set_index("Day", inplace= True)
print(df)


# In[66]:


df=df.rename(columns={'Users':"Visitors"})
print(df)


# In[ ]:




