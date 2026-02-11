#StrataScratch: Customer Tracking
#Level: Hard
#DataFrames: cust_tracking(cust_id,state,timestamp)
#Key Concepts: groupby, shift, sort_values, filtering

import pandas as pd

df = cust_tracking.sort_values(
    by=['cust_id', 'timestamp', 'state'],
    ascending=[True, True, False]
)

df['session_start'] = df.groupby('cust_id')['timestamp'].shift(1)

df = df[df['state'] == 0]

df['interval_hours'] = (
    df['timestamp'] - df['session_start']
).dt.total_seconds() / 3600

result = (
    df.groupby('cust_id')['interval_hours']
      .sum()
      .reset_index(name='total_hours')
)

result
# It was assumed that each session start (state=1) had a corresponding session end (state=0)