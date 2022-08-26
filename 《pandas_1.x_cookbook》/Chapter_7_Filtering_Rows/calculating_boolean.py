import pandas as pd
import numpy as np

movie = pd.read_csv(
    r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv',
    index_col='movie_title'
)
print(
    movie[['duration']].head()
)

movie_2_hours = movie['duration'] > 120
print(
    movie_2_hours,
    movie_2_hours.sum(),
    movie_2_hours.mean() * 100,
    movie_2_hours.describe(),
    movie_2_hours.value_counts(normalize=True),
    movie_2_hours.astype(int).describe(),
)

actors = movie[
    ['actor_1_facebook_likes','actor_2_facebook_likes']
].dropna()

print(
    (actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']
     ).mean()
)