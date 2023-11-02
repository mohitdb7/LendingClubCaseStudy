#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# In[2]:


df= pd.read_csv(r'C:\Users\Lenovo\Downloads\loan\loan.csv')


# In[3]:


df.head()


# In[4]:


# Understanding the dimensions of the file
df.shape


# In[5]:


#Understanding the columns and identifying number of missing values
100*df.isnull().mean()


# In[6]:


#Dropping columns which have more than 40% missing values
df=df.dropna(thresh=0.4*df.shape[0],axis=1)


# In[7]:


#Identifying unique values across all columns
df.nunique()


# In[8]:


# Getting the shape of the dataframe
df.shape


# In[9]:


#manual check for rge columns
print(df.columns)


# In[10]:


# Check for the columns datatypes
df.dtypes


# In[52]:


df['acc_now_delinq'].dtype


# In[53]:


df['desc']


# In[54]:


df['desc'].nunique()


# In[60]:


df=df.drop("desc",axis=1)


# In[58]:


df['emp_title'].nunique()


# In[71]:


df['emp_length'].nunique()


# In[64]:


df.head()


# In[72]:


df['pub_rec_bankruptcies'].nunique()


# In[73]:


df['revol_util'].nunique()


# In[77]:


thislist=[]
for columns in df:
    if df[columns].nunique()>10:
        thislist.append(columns)
print(thislist)
        


# In[78]:


df.nunique()


# In[ ]:




