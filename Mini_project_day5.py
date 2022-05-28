import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_excel("WHO_covid_cognizant.xlsx")
df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']
result = df.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(result) 
result.plot(x='Country/Region', y=['Confirmed','Deaths','Active','Recovered'],kind="bar",figsize=(16,16))
plt.ylabel("Count")
plt.legend()
plt.show()





