#!/usr/bin/env python
# coding: utf-8

# # Employee Attrition Analysis
# 
# 

# Employee Atrrition analysis is s type of behavioural analysis where we study the behaviour and characteristics of the the employee who left the organization and compare their characteristics with the the current employees to fint the employees who may leave the organization soon
# 

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("E:\\Ed - Byte\\Attrition.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


import plotly.graph_objects as go   # 3-D visualization library
import plotly.io as pio
pio.templates.default = 'plotly_white'


# In[6]:


df.isnull().sum()


# In[7]:


# filter the data to show only "yes" value in the Attrition column.


# In[8]:


attr_df = df[df['Attrition']== 'Yes']


# In[9]:


attr_df


# In[10]:


attr_df.shape


# # calculate the Attrition by Department

# In[11]:


attr_by_dpt = attr_df.groupby(['Department']).size()
attr_by_dpt


# In[12]:


attr_by_dpt = attr_df.groupby(['Department']).size().reset_index()
attr_by_dpt   #output into the Dataframe 


# In[13]:


attr_by_dpt = attr_df.groupby(['Department']).size().reset_index(name = 'count')
attr_by_dpt   #output into the Dataframe 


# In[14]:


fig1 = go.Figure(data = [go.Pie(
labels = attr_by_dpt['Department'],
values = attr_by_dpt['count'],
hole = 0.4,
marker = dict(colors = ['orange','yellow']),
textposition = 'inside')])


# In[15]:


fig1.update_layout(title = "Attrition by Department")
fig1.show()


# #  Attrition by Education field

# In[16]:


attr_by_edu = attr_df.groupby(['EducationField']).size().reset_index(name = "count")
attr_by_edu


# In[17]:


fig2 = go.Figure(data = [go.Pie(
labels = attr_by_edu['EducationField'],
values = attr_by_edu['count'],
hole = 0.4,
marker = dict(colors = ['orange','yellow']),
textposition = 'inside')])


# In[18]:


fig2.update_layout(title = "Attrition by Education")
fig2.show()


# # Now lets analyse the percetage of attrition by number of years at the company

# In[19]:


attr_df.columns


# In[20]:


attr_by_yrs = attr_df.groupby(['YearsAtCompany']).size().reset_index(name="count")
attr_by_yrs


# In[21]:


fig3 = go.Figure(data = [go.Pie(
labels = attr_by_yrs['YearsAtCompany'],
values = attr_by_yrs['count'],
hole = 0.4,
marker = dict(colors = ['orange','yellow']),
textposition = 'inside')])


# In[22]:


fig3.update_layout(title = "Attrition by Years in company")
fig3.show()


# # Analyze Attrition  by Promotion of employees

# In[23]:


attr_by_promo = attr_df.groupby(['YearsSinceLastPromotion']).size().reset_index(name = 'count')
attr_by_promo 


# # Lets analyze Attrition by Gender

# In[24]:


attr_by_gender = attr_df.groupby(['Gender']).size().reset_index(name = 'count')
attr_by_gender


# In[25]:


fig4 = go.Figure(data = [go.Pie(
labels = attr_by_gender['Gender'],
values = attr_by_gender['Gender'],
hole = 0.4,
marker = dict(colors = ['orange','yellow']),
textposition = 'inside')])


# In[26]:


fig4.update_layout(title = 'Attrition by Gender')
fig4.show()


# # Now Analyze the Attrition by Relationship between monthly income and age of the employees.

# In[27]:


import plotly.express as px


# In[28]:


df.columns


# In[29]:


fig5 = px.scatter(df,
                 x = "Age",
                 y = 'MonthlyIncome',
                 color = "Attrition",
                 trendline = "ols")
fig5.update_layout(title = "Age Vs Monthly Income by Attrition")
fig5.show()


# In[30]:


# we can see that the age of the person increases, monthaly income increases.
# we can also see a high rate of attrition among the employees with
# with low monthly incomes.

