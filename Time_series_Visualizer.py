import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = ['date'])
df
# Clean data
top_percentile = df.value.quantile(0.975)
bottom_percentile = df.value.quantile(0.025)
df = df[((df.value > bottom_percentile) & (df.value < top_percentile))]
df
#plotting page views VS date
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(df.index, df.value, color = "red")
ax.set_xlabel('Date')
ax.set_ylabel('Page Views')
ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
plt.show()
df.loc[:, 'Month'] = df.index.month
df.loc[:, 'Year'] = df.index.year
df
df_bar = df.groupby(['Month','Year']).value.mean()
fig = df_bar.unstack(0).plot.bar(figsize=(14,7))
fig.set_xlabel('Years')
fig.set_ylabel('Average Page Views')
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
plt.legend(fontsize = 10, labels = months)
plt.show()
plt.show()
fig, axes = plt.subplots(1, 2)
fig.set_figwidth(20)
fig.set_figheight(10)

ax1 = sns.boxplot(x="Month", y="value", data=df, ax = axes[0])
ax1.set_xlabel('Month')
ax1.set_ylabel('Page Views')
ax1.set_title("Month-wise Box Plot (Seasonality)")

ax2 = sns.boxplot(x="Year", y="value", data=df, ax = axes[1])
ax2.set_xlabel('Year')
ax2.set_ylabel('Page Views')
ax2.set_title("Year-wise Box Plot (Trend)")

plt.show()
