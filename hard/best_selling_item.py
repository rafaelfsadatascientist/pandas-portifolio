#StrataScratch: Best Selling Item
#Level: Hard
#DataFrames: online_retail(country,customerid,description,invoicedate,invoiceno,quantity,stockcode,unitprice)
#Key Concepts: ranks, groupby, sort_values

import pandas as pd

df = online_retail

df = df[df['quantity'] > 0]

df['total_paid'] = df['unitprice'] * df['quantity']
df['month'] = df['invoicedate'].dt.month

df = (
    df
    .groupby(['description', 'month'])['total_paid']
    .sum().reset_index()
    .sort_values(['month', 'total_paid'], ascending=[True, False])
)

df['rank'] = (
    df
    .groupby('month')['total_paid']
    .rank(method='dense', ascending=False)
)

df[df['rank'] == 1][['description', 'month', 'total_paid']]