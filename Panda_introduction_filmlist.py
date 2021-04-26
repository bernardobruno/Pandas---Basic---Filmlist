#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PANDAS --- from the data file (values and keys separeted by commas)


# In[4]:


import pandas as pd


# In[39]:


filmlist=pd.read_csv("filmlist.csv")  # ---> pd = pandas (up to you which one to choose)


# In[6]:


filmlist.head()


# In[7]:


print("First 10 records")
filmlist.head(10)


# In[10]:


filmlist.tail()


# In[14]:


#data.head and data subset

list_columns = ['Film', 'Year']
filmlist[list_columns]


# ### 3 hashes and run ---> to get a Título em Negrito

# In[16]:


filmlist['Genre'].value_counts()


# In[17]:


filmlist['Film'].value_counts()


# In[18]:


filmlist['Year'].value_counts()


# In[20]:


filmlist.head(2)


# In[21]:


filmlist['new_column'] =  "new column" ### DEFINE THE COLUMN LATER


# In[22]:


filmlist.head(10)


# ### INFORMATION

# In[24]:


filmlist.info()


# In[26]:


filmlist.shape ### ---> SHAPE OF DATA (ROWS, COLUMNS)


# In[40]:



# ---> examples of data cleaning 

filmlist.sort_values(by = 'Year')


# In[42]:


filmlist.sort_values(by = 'Year', ignore_index = True, ascending = False)


# In[45]:


filmlist.sort_values(by = ['Year', 'Profitability'], ignore_index = True, ascending = [True, False])


# In[ ]:





# In[46]:


x = ['Film', 'Genre', 'Lead Studio', 'Audience score %', 'Profitability', 'Rotten Tomatos %', 'Worldwide Gross', 'Year']


# ### Filtering th data 

# In[48]:


filmlist_grp = filmlist.groupby ('Year')


# In[49]:


filmlist_grp


# 

# In[50]:


filmlist_2008 = filmlist_grp.get_group(2008)
filmlist_2008.head()


# In[52]:


filmlist[filmlist['Year'] == 2008]


# In[ ]:




