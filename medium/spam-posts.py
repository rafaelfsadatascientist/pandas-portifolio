#StrataScratch: Spam Posts
#Level: Medium
#DataFrames: facebook_posts(post_id,poster,post_text,post_keywords,post_date) & facebook_post_reviews(post_id,viewer_id)
#Key Concepts: merge, agg, groupby, sort_values

import pandas as pd

merged_df = pd.merge(
    facebook_posts, 
    facebook_post_views, 
    on='post_id', 
    how='inner'
)

merged_df['is_spam'] = merged_df['post_keywords'].str.contains('spam')

daily_summary = (
    merged_df
    .groupby('post_date')
    .agg({
        'post_id': 'count',
        'is_spam': 'sum'
    })
    .rename(columns={
        'post_id': 'total_posts',
        'is_spam': 'total_spam'
    })
    .reset_index()
)

daily_summary['spam_share'] = daily_summary['total_spam'] / daily_summary['total_posts'] * 100

result = daily_summary[['post_date', 'spam_share']]

result
