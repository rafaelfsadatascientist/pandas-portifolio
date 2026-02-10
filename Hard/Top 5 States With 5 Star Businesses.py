--StrataScratch: Top 5 States With 5 Star Businesses
--Level: Hard
--DataFrames: yelp_business(business_id, name, neighborhood, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, categories)
--Key Concepts: ranks, groupby, sort_values, rename, astype

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business
df['five_stars'] = (df['stars'] == 5).astype(int)
top5_states = (
    df.groupby('state', as_index=False)['five_stars'].sum()
      .rename(columns={'five_stars': 'stars_count'})
      .sort_values(by=['stars_count', 'state'], ascending=[False, True])
)
top5_states['rank'] = top5_states['stars_count'].rank(method='dense', ascending=False)
top5_states = top5_states[top5_states['rank'] <= 5][['state', 'stars_count']]
top5_states