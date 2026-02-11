#StrataScratch: Consecutive Days
#Level: Hard
#DataFrames: sf_events(record_date,account_id,user_id)
#Key Concepts: shift, drop_duplicates, filtering, datetime arithmetic

# If a user was active for more than 3 consecutive days,
# then in particular the user was active for at least 3 consecutive days.
# Therefore, it is enough to find any "middle day" where the previous
# and the next days are exactly 1 day apart.
import pandas as pd
df = sf_events.sort_values(['user_id', 'record_date'])
df['prev_day'] = df.groupby('user_id')['record_date'].shift(1)
df['next_day'] = df.groupby('user_id')['record_date'].shift(-1)

df['diff_prev'] = (df['record_date'] - df['prev_day']).dt.days
df['diff_next'] = (df['next_day'] - df['record_date']).dt.days

result = (
    df[(df['diff_prev'] == 1) & (df['diff_next'] == 1)]
    ['user_id']
    .drop_duplicates()
)

result
