#StrataScratch: Find the genre of the person with the most number of oscar winnings
#Level: Hard
#DataFrames: oscar_nominees(year,category,nominee,movie,winner,id) & nominee_information(name,amg_person_id,top_genre,birthday,id)
#Key Concepts: groupby, iloc, sort_values, merge, astype

import pandas as pd

df = pd.merge(
    oscar_nominees,
    nominee_information,
    left_on='nominee',
    right_on='name',
    how='inner'
)

df['winner'] = df['winner'].astype(int)

df = (
    df.groupby(['name', 'top_genre'])['winner']
      .sum()
      .reset_index()
      .rename(columns={'winner': 'number_of_oscar_wins'})
      .sort_values(
          by=['number_of_oscar_wins', 'name'],
          ascending=[False, True]
      )
)

result = df.iloc[0]['top_genre']
