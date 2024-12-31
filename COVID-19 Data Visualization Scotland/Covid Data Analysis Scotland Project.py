#!/usr/bin/env python
# coding: utf-8

# 
# 

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt 


# In[4]:


import seaborn as sns


# In[5]:


import plotly.express as px


# In[6]:


from plotly.subplots import make_subplots


# In[7]:


from datetime import datetime


# In[8]:


#Import first dataset
covid_df = pd.read_csv("C:/Users/fokst/OneDrive/Desktop/COVID-19 Data Visualization UK/covid-19-totals-scotland.csv")


# In[145]:


#Return first 10 rows
covid_df.head(10)


# In[146]:


covid_df.info


# In[147]:


#Summary statistics for numerical columns in the dataframe
covid_df.describe()


# In[148]:


#Import second dataset
vaccine_df = pd.read_csv("C:/Users/fokst/OneDrive/Desktop/COVID-19 Data Visualization UK/Vaccine Data 1.csv")


# In[149]:


vaccine_df.head(7)


# In[150]:


#Generate active cases
covid_df["Active Cases"] = covid_df["ConfirmedCases"] + covid_df["Deaths"]
covid_df.tail()


# In[151]:


statewise = pd.pivot_table(covid_df, values = ["ConfirmedCases", "Deaths", "Tests"], index = "Date", aggfunc = max)


# In[152]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["ConfirmedCases"]


# In[153]:


statewise = statewise.sort_values(by = "ConfirmedCases", ascending = False)


# In[154]:


#cmap = colour map #matplotlib #08/01/2020 death info missing
statewise.style.background_gradient(cmap = "cubehelix" )


# In[155]:


#Top 10 dates with the highest number of active cases

top_10_active_cases = covid_df.groupby(by = "Date").max()[["Active Cases"]].sort_values(by = ["Active Cases"], ascending = False).reset_index()


# In[156]:


#Creating figure object 
fig = plt.figure(figsize = (16,9))


# In[157]:


#Creating plot 
plt.title("Top 10 dates with the highest recorded number of active cases", size = 25)


# In[158]:


#Defining axis using data
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active Cases", x = "Date", linewidth = 2, edgecolor = "black")


# In[159]:


#All combined

top_10_active_cases = covid_df.groupby(by = "Date").max()[["Active Cases"]].sort_values(by = ["Active Cases"], ascending = False).reset_index()
fig = plt.figure(figsize = (16,9))
plt.title("Top 10 dates with the highest recorded number of active cases", size = 25)
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active Cases", x = "Date", linewidth = 2, edgecolor = "black")


plt.xlabel("Date")
plt.ylabel("Total Active Cases")
plt.show()


# In[160]:


#Top 10 dates with highest recorded deaths

top_10_deaths = covid_df.groupby(by = "Date").max()[["Deaths"]].sort_values(by = "Deaths", ascending = False).reset_index()

fig = plt.figure(figsize=(18,5))

plt.title("Top 10 dates with highest recorded deaths", size = 25)

ax = sns.barplot(data = top_10_deaths.iloc[:10], y = "Deaths", x = "Date", linewidth = 2, edgecolor = "black")

plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.show()


# In[161]:


#Growth trend of the top 5 active cases of Covid in Scotland

fig = plt.figure(figsize = (12,6))

ax = sns.lineplot(data = covid_df[covid_df["Date"].isin(["2020-07-31", "2020-07-23", "2020-07-16", "2020-07-17", "2020-07-18", "2020-07-19"])], x = "Date", y = "Active Cases")

ax.set_title("Top 5 Active Cases of Covid in Scotland", size = 16)


# In[162]:


vaccine_df.head()


# In[163]:


#Incorporating rename function
vaccine_df.rename(columns = {"Date" : "Vaccine Date"}, inplace = True)
vaccine_df.head(10)


# In[164]:


vaccine_df.info()


# In[173]:


#Checks which values are null/not given. 0=notnull, have value=null
vaccine_df.isnull().sum()


# In[166]:


#Drop/remove columns
vaccination = vaccine_df.drop(columns = ["Country", "_id", "PercentCoverage", "CumulativeNumberVaccinated", "CumulativePercentCoverage"], axis = 1)
vaccination.head(10)


# In[167]:


#Dates with the most number of vaccination
max_vac = vaccination.groupby("Vaccine Date")["NumberVaccinated"].sum().to_frame("NumberVaccinated")
max_vac = max_vac.sort_values("NumberVaccinated", ascending = False)[:5]
max_vac


# In[168]:


#Plot, Axis Data, and Figure objects combined
fig = plt.figure(figsize=(10,5))
plt.title("Top 5 Dates with the Most Number of Vaccination", size = 20)
ax = sns.barplot(data = max_vac.iloc[:10], y = max_vac.NumberVaccinated, x = max_vac.index, linewidth = 2, edgecolor = "black")
plt.xlabel("Date")
plt.ylabel("Vaccination")
plt.show()


# In[169]:


#Dates with the least number of vaccination
min_vac = vaccination.groupby("Vaccine Date")["NumberVaccinated"].sum().to_frame("NumberVaccinated")
min_vac = min_vac.sort_values("NumberVaccinated", ascending = True)[:5]
min_vac

fig = plt.figure(figsize=(10,5))
plt.title("Top 5 Dates with the Least Number of Vaccination", size = 20)
ax = sns.barplot(data = min_vac.iloc[:10], y = min_vac.NumberVaccinated, x = min_vac.index, linewidth = 2, edgecolor = "black")
plt.xlabel("Date")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




