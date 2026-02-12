#StrataScratch: New Products
#Level: Medium
#DataFrames: car_launches(year,company_name,product_name)
#Key Concepts: merge, groupby

import pandas as pd

df = car_launches

companies = df[['company_name']].drop_duplicates()

df_2019 = (
    df[df['year'] == 2019]
    .groupby('company_name')['product_name']
    .count()
    .reset_index()
    .rename({'product_name': 'number_of_products_launched_2019'}, axis=1)
)

df_2020 = (
    df[df['year'] == 2020]
    .groupby('company_name')['product_name']
    .count()
    .reset_index()
    .rename({'product_name': 'number_of_products_launched_2020'}, axis=1)
)

df_merge = pd.merge(
    companies,
    df_2019,
    left_on='company_name',
    right_on='company_name',
    how='left'
)

df_final = pd.merge(
    df_merge,
    df_2020,
    left_on='company_name',
    right_on='company_name',
    how='left'
)

df_final['number_of_products_launched_2019'] = df_final['number_of_products_launched_2019'].fillna(0)
df_final['number_of_products_launched_2020'] = df_final['number_of_products_launched_2020'].fillna(0)

df_final['net_difference'] = (
    df_final['number_of_products_launched_2020'] - df_final['number_of_products_launched_2019']
)

df_final[['company_name', 'net_difference']]