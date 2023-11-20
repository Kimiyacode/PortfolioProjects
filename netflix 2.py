#!/usr/bin/env python
# coding: utf-8

# # Loading packages

# In[92]:


import pandas as pd
import numpy as np
import plotly.express as px
import klib 
import matplotlib.pylab as plt #visualization
import seaborn as sns #for exploratory plots
from matplotlib import *
from encodings.aliases import aliases 
plt.style.use('ggplot')
pd.set_option('max_columns',50)


# # Importing dataframe

# In[93]:


df = pd.read_csv('netflix_titles.csv')


# # Quick Overview / Understanding of our data

# In[7]:


df.shape


# In[9]:


df.info() #all data in object type, only release year as integer, show_id is our primary


# In[10]:


df.columns


# In[12]:


df.head()


# In[14]:


df.describe() #did not give us much since only int. Movies ranging between year 1925-2021, mostly relative new movies in our dataset


# # Data Cleaning & Preparation

# In[ ]:


# Examine if we need to drop irrelevant rows or columns
# Correcting inaccuracies or errors in the data
# Renaming columns
# Removing or imputing missing values
# Checking for duplicates


# In[15]:


df.head(20) #getting an idea how to clean this data


# In[23]:


df.columns


# In[94]:


df.drop('description', axis=1, inplace=True) #deleting a column we don't need


# In[29]:


df.columns


# In[31]:


df.dtypes #date should be in integer form


# In[95]:


df['date_added'] = pd.to_datetime(df['date_added']) #transforming the datatype


# In[38]:


df.dtypes #successfully added


# In[39]:


df.head() #just doublechecking, looks correct


# In[96]:


# We need to rename multiple columns since it is annoying and unclear

df.columns


# In[97]:


df = df.rename(columns={'type':'film_category',
                   'title':'film_title', 
                   'director':'film_director',
                   'cast':'actors',
                   'country': 'production_country',
                   'rating':'classification',
                   'listed_in':'genres'})


# In[48]:


df.head() #looks correct


# ## Handling missing values

# In[50]:


# Missing values
df.isna().sum() #film director have many missing values, it will not impact our analysis, same with actors


# In[98]:


df.drop('film_director', axis=1, inplace=True) #deleting column we won't need


# In[99]:


df.drop('actors', axis=1, inplace=True) #deleting column we won't need


# In[100]:


df.isna().sum()


# In[ ]:





# In[106]:


# Filling different values in null in different columns, since this is 10% of our dataset we want to keep the row but will fill the values with unknown for visualization purposes when doing graphs later
df2 = df.fillna({'production_country': 'unknown',
                'classification':'unknown'}, 
                 inplace=True)


# In[109]:


df.head() #operation successful


# In[110]:


df.isna().sum() #choosing to fill date_added with the mean of its column,


# In[ ]:


df3 = df.dropna() #drops rows that contains null values basically


# In[80]:


#Filling up the null value with the mean of its column
df2['date_added'].fillna(df3['date_added'].mean(), inplace=True)


# In[ ]:





# In[ ]:




