##StrataScratch: Titanic Survivors and Non-Survivors
##Level: Medium
##DataFrames: titanic(passengerid, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked)
##Key Concepts: merges, filtering

import pandas as pd

df = titanic

first_class  = df[df['pclass'] == 1]
second_class = df[df['pclass'] == 2]
third_class  = df[df['pclass'] == 3]

first_class  = first_class.groupby('survived')['passengerid'].count().reset_index()
first_class  = first_class.rename({'passengerid': 'First Class'}, axis=1)

second_class = second_class.groupby('survived')['passengerid'].count().reset_index()
second_class = second_class.rename({'passengerid': 'Second Class'}, axis=1)

third_class  = third_class.groupby('survived')['passengerid'].count().reset_index()
third_class  = third_class.rename({'passengerid': 'Third Class'}, axis=1)

merged_df = pd.merge(first_class, second_class, left_on='survived',right_on='survived', how='inner')
merged_df = pd.merge(merged_df, third_class, left_on='survived', right_on='survived', how='inner')

merged_df