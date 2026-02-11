#StrataScratch: Election Results
#Level: Medium
#DataFrames: voting_results(voter,candidate)
#Key Concepts: ranks, groupby, sort_values, transform

import pandas as pd

df = voting_results[voting_results['candidate'].notna()]
df = df.sort_values(by='voter', ascending=True)

df['number_of_votes'] = df.groupby('voter')['candidate'].transform('count')
df['vote_value'] = round(1 / df['number_of_votes'], 3)

result = (
    df.groupby('candidate')['vote_value']
      .sum()
      .reset_index()
)

result = result.sort_values(by='vote_value', ascending=False)
result['rank'] = result['vote_value'].rank(method='dense', ascending=False)

winners = result[result['rank'] == 1]['candidate']
winners