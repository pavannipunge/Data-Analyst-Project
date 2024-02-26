#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("E:\\Ed - Byte\\click.csv")


# In[3]:


df.head()


# In[4]:


import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"


# #  the "Clicked on Ad" column contain 0 and 1 values where 0 means not clicked and 1 means clicked.  we will transform these values into "YES" and "No".
# 

# In[5]:


df['Clicked on Ad'] = df['Clicked on Ad'].map({0:'No',
                                              1:'Yes'})


# In[6]:


df.head()


# #  Now lets analyze the click through rate based on the time spent by the users on website.

# In[7]:


fig1 = px.box(df,
             x = "Daily Time Spent on Site",
             color = "Clicked on Ad",
             title = "Click Through Rate Based Time Spent on Site",
             color_discrete_map = {'Yes':'Blue',
                                  'No':'Red'})


# In[8]:


fig1.update_traces(quartilemethod = "exclusive") 
fig1.show() 


# # Now Analyze the click through rate based on the daily internet usage of the user.

# In[9]:


fig = px.box(df,
            x = "Daily Internet Usage",
            color = "Clicked on Ad",
            title = "Click Through Rate Based on Daily Internet Usage",
            color_discrete_map = {'Yes':'Blue', 'No':'Red'})


# In[10]:


fig.update_traces(quartilemethod = "exclusive") 
fig.show() 


# #  Now Analyze the click through rate based on the age of the user

# In[11]:


fig2 = px.box(df,
             x = "Age",
             color = "Clicked on Ad",
             title = "Click Through Rate Based on Age",
             color_discrete_map = {'Yes':'Black' , 'No':'Red'})


# In[12]:


fig2.update_traces(quartilemethod = "exclusive")
fig2.show() 


# # Now lets analyze the click through rate based on income of the users.

# In[13]:


fig3 = px.box(df,
             x = "Area Income",
             color = "Clicked on Ad",
             title = "Click Through Rate Based on Income",
             color_discrete_map = {'Yes':'Black' , 'No':'Red'})


# In[14]:


fig3.update_traces(quartilemethod = "exclusive")
fig3.show() 


# #  Now calculate the click through rate of ads

# In[15]:


df['Clicked on Ad'].value_counts() 


# In[16]:


df.shape 


# In[17]:


click_through_rate_yes = 4917/10000 * 100 
click_through_rate_yes


# In[18]:


click_through_rate_No = 5083/10000 * 100 
click_through_rate_No


# In[ ]:




