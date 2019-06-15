#!/usr/bin/env python
# coding: utf-8

# ## Rapid Information Factory with Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a set of research books and needs to be accepted as part of that copyright.

# ### 300-Crawler-Input-Template-000001

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# In[2]:


import pandas as pd
import os


# In[3]:


def InputData():
    dirname='../../../../100-DL/100-Raw-Zone/0100-External/100-Golden-Source/000005-Data-Source-F/'
    filename='First-Name-Boy-000001.csv'
    fullfilename=os.path.abspath(os.path.join(dirname, filename))
    print(fullfilename)
    dfIn=pd.read_csv(
        fullfilename,
        header=0,
        sep=',',
        encoding='latin1',
        skip_blank_lines=True,
        quotechar='"',
        verbose=False,
        low_memory=True
    )
    return dfIn


# In[4]:


InData = InputData()


# In[5]:


InData.shape


# In[6]:


InData


# In[7]:


def ProcessData(df0):
    df1 = df0.loc[df0.id.notnull()]
    return df1


# In[8]:


ProcData = ProcessData(InData)


# In[9]:


ProcData.shape


# In[10]:


ProcData


# In[11]:


def OutputData(df):
    dirname='../../../../100-DL/100-Raw-Zone/0200-Internal/000100-CSV/'
    filename='First-Name-Boy-000001.csv'
    fullfilename=os.path.abspath(os.path.join(dirname, filename))
    print(fullfilename)
    df.to_csv(
        fullfilename,
        header=0,
        index=False,
        sep=',',
        encoding='latin1',
        quotechar='"'
    )


# In[12]:


OutputData(ProcData)


# # Run Time

# In[13]:


nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

