import pandas as pd
import matplotlib.pyplot as plt
movie = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv',
                    index_col='movie_title')
fb_likes = movie['actor_1_facebook_likes'].dropna()
print(
    fb_likes.head()
)
print(
    fb_likes.describe()
)

fig,ax = plt.subplots(figsize=(10,8))
fb_likes.hist(ax=ax)
fig.savefig(
    'c7-hist.png',dpi=300
)
criteria_high = fb_likes < 20_000
print(
    criteria_high.mean().round(2)
)
print(
    fb_likes.where(criteria_high).head()
)
print(
    fb_likes.where(criteria_high,other=20000).head()
)