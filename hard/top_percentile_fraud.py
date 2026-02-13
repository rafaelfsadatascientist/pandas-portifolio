##StrataScratch: Top Percentile Fraud
##Level: Hard
##DataFrames: fraud_score(policy_num,state,claim_cost,fraud_score)
##Key Concepts: numpy, percentile, quantile, apply, transform, merge, groupby

import pandas as pd
import numpy as np

percentile_by_state = (
    fraud_score
    .groupby('state')['fraud_score']
    .apply(lambda x: np.percentile(x, 95))
    .reset_index()
)
percentile_by_state.rename({'fraud_score': 'percentile'}, axis=1, inplace=True)

df = pd.merge(
    fraud_score,
    percentile_by_state,
    on='state',
    how='inner'
)

df = df[df['fraud_score'] >= df['percentile']]

df[['policy_num', 'state', 'claim_cost', 'fraud_score']]

# Note: we could have avoided the merge using transform and could calculate the percentile using quantile
