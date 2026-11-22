#!/usr/bin/env python
# coding: utf-8

# # City Data Analysis
# 
# ## Introduction
# This notebook analyzes city temperature and population data.
# 
# ## Objectives
# - Load the dataset
# - Analyze temperatures
# - Compare cities
# - Visualize data
# 
# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


print("Dataset shape:", df.shape)

print("\nStatistical summary:")
print(df.describe())


# In[4]:


df = pd.read_csv("../data/city_data.csv")
print(df)


# In[5]:


print("Dataset shape:", df.shape)

print("\nStatistical summary:")
print(df.describe())


# In[6]:


print("Average temperature:", df["Temperature"].mean())

print("Maximum temperature:", df["Temperature"].max())

print("Minimum temperature:", df["Temperature"].min())


# In[7]:


chennai = df[df["City"] == "Chennai"]

print(chennai)

print("Chennai average temperature:",
      chennai["Temperature"].mean())


# ## Conclusion
# 
# - Chennai appears twice in the dataset.
# - Chennai average temperature is 34.5°C.
# - Bangalore has the lowest temperature at 28°C.
# - Mumbai has the highest population at 20 million.
# - Overall average temperature is 31.67°C.

# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(df["City"], df["Temperature"])

plt.title("City Temperature Comparison")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")

plt.show()


# In[ ]:




