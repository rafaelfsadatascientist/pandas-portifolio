##StrataScratch: Largest Olympics
##Level: Medium
##DataFrames: olympics_athletes_events(id,name,sex,age,height,weight,team,noc,games,year,season,city,sport,event,medal)
##Key Concepts: groupby, rank, sort_values, filtering

import pandas as pd

df = (
    olympics_athletes_events
    .groupby(['year', 'season'])['id']
    .nunique()
    .reset_index()
    .rename({'id': 'athletes_count'},axis=1)
    .sort_values(by='athletes_count', ascending=False)
)

df['rank'] = df['athletes_count'].rank(method='dense', ascending=False)
df = df[df['rank'] == 1]
df['games'] = df['year'].astype(str) + ' ' + df['season']
df[['games','athletes_count']]
