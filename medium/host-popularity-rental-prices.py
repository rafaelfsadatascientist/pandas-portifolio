#StrataScratch: Host Popularity Rental Prices
#Level: Medium
#DataFrames: airbnb_host_searches(id, price, property_type, room_type, amenities, accommodates, bathrooms, bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,host_response_rate, host_since, neighbourhood, number_of_reviews, review_scores_rating, zipcode, bedrooms, beds)
#Key Concepts: apply, agg, groupby

import pandas as pd

def popularity(x):
    if x == 0:
        return 'New'
    elif 1 <= x <= 5:
        return 'Rising'
    elif 6 <= x <= 15:
        return 'Trending Up'
    elif 16 <= x <= 40:
        return 'Popular'
    else:
        return 'Hot'


df = airbnb_host_searches

df['host_popularity'] = df['number_of_reviews'].apply(popularity)

df = (
    df
    .groupby(['host_popularity'])['price']
    .agg(['max', 'min', 'mean'])
    .reset_index()
    .rename({
        'max': 'max_price',
        'min': 'min_price',
        'mean': 'mean_price'
    },axis=1)
)

df.sort_values(by=['min_price'], ascending=True)
