--StrataScratch: Highest Cost Orders
-- Dialect: PostgreSQL
--Level: Medium
--Tables: customers(address,city,first_name,id,last_name,phone_number) & orders(cust_id,id,order_date,order_details,total_order_cost)
--Key Concepts: merges, groupby, sort_values, ranks, between

import pandas as pd

df = pd.merge(
    customers,
    orders,
    left_on='id',
    right_on='cust_id',
    how='left'
)

df = df[df['order_date'].between('2019-02-01', '2019-05-01')]

df = df.groupby(['first_name', 'order_date'])['total_order_cost'].sum().reset_index()
df = df.rename(columns={'total_order_cost': 'total_orders_cost'})
df = df.sort_values(by=['order_date', 'total_orders_cost'], ascending=[True, False])

df['rank'] = df.groupby('order_date')['total_orders_cost'].rank(method='dense', ascending=False)
df = df[df['rank'] == 1]
df = df.rename({'total_orders_cost': 'max_cost'},axis=1)

df[['first_name', 'order_date', 'max_cost']]
