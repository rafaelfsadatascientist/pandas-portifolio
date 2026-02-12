#StrataScratch: Income By Title and Gender
#Level: Medium
#DataFrames: sf_employee(id,first_name,last_name,age,sex,employee_title,department,salary,target,email,city,address,manager_id) & sf_bonus(worker_ref_id,bonus)
#Key Concepts: merge, groupby, transform 

import pandas as pd

df = pd.merge(
    sf_employee,
    sf_bonus,
    left_on='id',
    right_on='worker_ref_id',
    how='inner'
)

df['total_bonus'] = df.groupby('id')['bonus'].transform('sum')
df['total_compensation'] = df['salary'] + df['total_bonus']

df = (
    df[['id', 'employee_title', 'sex', 'total_compensation']]
    .drop_duplicates()
)

result = (
    df.groupby(['employee_title', 'sex'])['total_compensation']
      .mean()
      .reset_index()
      .rename({'total_compensation': 'avg_total_comp'},axis=1)
)

