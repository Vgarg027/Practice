#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Loading the data 
# 

# In[2]:


femalesaged_df = pd.read_csv('females_aged_15_24_employment_rate_percent.csv')
malesaged_df = pd.read_csv('males_aged_15_24_employment_rate_percent.csv')
femaleworkers_df = pd.read_csv('female_service_workers_percent_of_female_employment.csv')
maleworkers_df= pd.read_csv('male_service_workers_percent_of_male_employment.csv')
# encoding = "ISO-8859-1" had to be added to the last three files due to an error of 'utf-8'


# In[3]:


femalesaged_df.head()


# In[4]:


malesaged_df.head()


# In[5]:


femaleworkers_df.head()


# In[6]:


femaleworkers_df.head()


# In[7]:


year = pd.Series(range(2000,2017)).astype(str)
femalesaged_df2 = pd.melt(femalesaged_df,id_vars=['country'],value_vars = year,var_name='Year',value_name='Female_Employee Age15-24')
femalesaged_df2.describe()


# In[8]:


year = pd.Series(range(2000,2017)).astype(str)
malesaged_df2 = pd.melt(malesaged_df,id_vars=['country'],value_vars = year,var_name='Year',value_name='Male_Employee Age15-24')
malesaged_df2.describe()


# In[9]:


malesaged_df2.head(20)


# In[10]:


femalesaged_df2.head(20)


# In[11]:


maleworkers_df.head()


# In[12]:


year = pd.Series(range(2000,2017)).astype(str)
maleworkers_df2 = pd.melt(maleworkers_df,id_vars=['country'],value_vars = year,var_name='Year',value_name='Male_service_workers')
maleworkers_df2.describe()


# In[13]:


year = pd.Series(range(2000,2017)).astype(str)
femaleworkers_df2 = pd.melt(femaleworkers_df,id_vars=['country'],value_vars = year,var_name='Year',value_name='female_service_workers')
femaleworkers_df2.describe()


# In[14]:


maleworkers_df2.head()


# In[15]:


data1_df1 = pd.merge(femaleworkers_df2,maleworkers_df2,  how='left', left_on=['country','Year'], right_on = ['country','Year'])
data1_df1.head()


# In[16]:


data2_df2 = pd.merge(femalesaged_df2, malesaged_df2, how='left', left_on=['country','Year'], right_on = ['country','Year'])
data2_df2.head()


# In[17]:


commbinedata_df = pd.merge(data2_df2, data1_df1,  how='left', left_on=['country','Year'], right_on = ['country','Year'])
commbinedata_df.head(50)


# In[18]:


plt.show()


# In[19]:


#check missing values
commbinedata_df.columns[commbinedata_df.isnull().any()]


# In[20]:


commbinedata_df.info()


# In[21]:


commbinedata_df.dropna(inplace=True)


# In[22]:


print(commbinedata_df.duplicated().sum())


# In[23]:


commbinedata_df.describe()


# # Q1: how much is  the number of Female workers compare to male employees in Age15-24 ?

# In[37]:


x1 = femalesaged_df2['Female_Employee Age15-24']

args = dict(alpha=0.5, bins=100)

plt.hist(x1, **args, color='r', label='Percent rate')
plt.gca().set(title='Female_Employee Age15-24', ylabel='Frequency')
plt.xlim(5,80)
plt.legend();


# In[38]:


x2 = malesaged_df2['Male_Employee Age15-24']

args = dict(alpha=0.5, bins=100)

plt.hist(x2, **args, color='b', label='Percent rate')
plt.gca().set(title='Male_Employee Age15-24', ylabel='Frequency')
plt.xlim(5,80)
plt.legend();


# In[35]:


sum_df = data1_df1.groupby('Year', as_index= False).sum()
sum_df.head()


# In[36]:


avg_df.plot(x='Year', y='female_service_workers',visible=True,figsize=(10,5))

plt.suptitle('total Females working in service sector over 2000-2017', fontsize=17)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Females working in service sector the world per year', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
x_axis = pd.Series(range(2000,2017)).astype(str)
plt.xticks( np.arange(17), x_axis)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




