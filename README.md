# COVID 19 Data Visualisation (2020)

#create summary using pivot table
summary = pd.pivot_table(covid_df, values = ["ConfirmedCases", "Deaths", "Tests"], index = "Date", aggfunc = max)

#mortality rate
summary["Mortality Rate"] = summary["Deaths"]*100/summary["ConfirmedCases"]

summary = summary.sort_values(by = "ConfirmedCases", ascending = False)

#cmap = colour map 
summary.style.background_gradient(cmap = "cubehelix" )


## Image Preview
![image alt]()


