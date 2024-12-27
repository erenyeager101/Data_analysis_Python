import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Import data
df = pd.read_csv("medical_examination.csv")
df.describe()
BMI = df['weight']/((df['height']/100)**2) 
BMI = BMI > 25
# Add 'overweight' column
df['overweight'] = BMI
df.overweight = df.overweight.astype(int)
# Normalize data by making 0 always good and 1 always bad. 
#If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].replace([1],0)
df['gluc'] = df['gluc'].replace([1],0)
df['cholesterol'] = df['cholesterol'].replace([2,3], value=1)
df['gluc'] = df['gluc'].replace([2,3], value=1)
df.cholesterol.value_counts()
df.head(5)
var = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=var)
df_cat
graph = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")
graph.set_ylabels('total', fontsize=10)
df = df.loc[(df.ap_lo <= df.ap_hi)
                 & (df.height >= df.height.quantile(0.025))
                 & (df.height <= df.height.quantile(0.975))
                 & (df.weight >= df.weight.quantile(0.025))
                 & (df.weight <= df.weight.quantile(0.975)), :]
f, ax = plt.subplots(figsize=(15, 10))
corr = df.corr()
mask = np.triu(corr)
ax = sns.heatmap(corr, mask=mask, annot=True, cmap='mako', fmt=".1f")
plt.show()
