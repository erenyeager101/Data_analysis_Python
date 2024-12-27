import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
#Use Pandas to import the data from epa-sea-level.csv.
df = pd.read_csv('epa-sea-level.csv')
df.head()
fig, ax = plt.subplots()
ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
plt.show()
line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
b1, b0, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
b0 + b1 * 2050
#Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
fig, ax = plt.subplots()
ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
plt.plot(df["Year"], line1.intercept + line1.slope*df["Year"], 'r', label='fitted line')
ax.set_xlabel("Year")
ax.set_ylabel("Sea Level (inches)")
ax.set_title("Rise in Sea Level")
plt.legend()
plt.show()
df_2000 = df[df["Year"] > 2000]
#Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
line2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
b1, b0, r_value, p_value, std_err = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
b0 + b1 * 2050
#Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
#The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
fig, ax = plt.subplots()
ax.scatter(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
plt.plot(df_2000["Year"], line2.intercept + line2.slope*df_2000["Year"], 'r', label='fitted line')
ax.set_xlabel("Year")
ax.set_ylabel("Sea Level (inches)")
ax.set_title("Rise in Sea Level")
plt.legend()
plt.show()
