#!/usr/bin/env python
# coding: utf-8

# # Pandas Functions

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
df


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.sample()


# In[10]:


df.sample(2)


# # Pandas Input/Output Tools

# In[13]:


df=pd.read_csv('hrdata.csv')
print(df)


# In[15]:


print(type(df['HireDate'][0]))


# In[16]:


df=pd.read_csv('hrdata.csv', index_col='Name', parse_dates=['HireDate'])


# In[17]:


print(df)


# In[19]:


print(type(df['HireDate'][0]))
print(type(df['HireDate'][2]))


# In[23]:


df=pd.read_csv('hrdata.csv',
               index_col='Employee',
               parse_dates=['Hired'],
               header=0,
               names=['Employee', 'Hired', 'Salary', 'Sickdays', 'Balance'])
print(df)


# In[24]:


df
df.to_csv('hrdata_modified.csv')


# In[28]:


dfh=pd.read_csv('hrdata_modified.csv')
dfh


# In[30]:


dfh['Salary'].plot.bar()


# # Reading TSV format file

# In[32]:


import pandas


# In[33]:


get_ipython().run_line_magic('pinfo', 'pandas.read_csv')


# In[34]:


#Tab Saperated values


# In[35]:


import pandas as pd


# In[37]:


dfh=pd.read_csv('agedata.tsv',sep='\t')


# In[38]:


print(dfh)


# In[40]:


#https://github.com/StephenJohn1188/CSV-file1/blob/main/agedata.tsv


# # Web API

# In[42]:


get_ipython().system('pip install requests')


# In[44]:


import requests


# In[47]:


response=requests.get("https://jarasoinstitute.com/")


# In[48]:


response.status_code


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




