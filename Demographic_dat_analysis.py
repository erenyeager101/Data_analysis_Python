import numpy as np
import pandas as pd
df = pd.read_csv("adult.data.csv")
#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
df.race.value_counts()
#What is the average age of men?
round(df.loc[df['sex'] == "Male", 'age'].mean(),1)
#What is the percentage of people who have a Bachelor's degree?
round((df.loc[df['education'] =="Bachelors", 'education'].count() / df.shape[0]) * 100,1)
#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
round(df[df.education.isin(filters)].salary.value_counts(normalize=True)[1]*100,1)
#What percentage of people without advanced education make more than 50K?
round(df[~df.education.isin(filters)].salary.value_counts(normalize=True)[1]*100,1)
#What is the minimum number of hours a person works per week?
df['hours-per-week'].min()
#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
round(df[df['hours-per-week']==df['hours-per-week'].min()].salary.value_counts(normalize=True)[1]*100,1)
#What country has the highest percentage of people that earn >50K and what is that percentage?
richCounts = df[df.salary==">50K"].groupby(['native-country']).count().salary
totalCounts = df['native-country'].value_counts()
result = richCounts/totalCounts*100
result.idxmax()
#Identify the most popular occupation for those who earn >50K in India.
round(result.max(),1)
df[(df['native-country'] == "India") & (df['salary']==">50K")].occupation.value_counts().idxmax()
