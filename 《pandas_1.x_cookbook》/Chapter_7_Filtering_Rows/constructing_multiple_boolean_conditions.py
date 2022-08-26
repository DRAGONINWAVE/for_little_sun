import pandas as pd

movie = pd.read_csv(
    r'D:\python3.10\Pandas-Cookbook-master\data\movie.csv',
    index_col='movie_title'
)
criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000 |
             (movie.title_year > 2009)
             )
criteria_final = criteria1 & criteria2 & criteria3
print(
    criteria_final.head()
)

crit_b1 = movie.imdb_score < 5
crit_b2 = movie.content_rating == 'R'
crit_b3 = (
    (movie.title_year >= 2000) & ( movie.title_year <= 2010)
)

final_crit_b = crit_b1 & crit_b2 & crit_b3
final_crit_all = criteria_final | final_crit_b
print(
    final_crit_all.head()
)
print(
    movie[final_crit_b].head()
)
print(
    movie.loc[final_crit_all].head()
)
cols = ['imdb_score', 'content_rating','title_year']
movie_filtered = movie.loc[final_crit_all,cols]
print(
    movie_filtered.head(10)
)
print(
    movie.iloc[final_crit_all.to_numpy()]
)