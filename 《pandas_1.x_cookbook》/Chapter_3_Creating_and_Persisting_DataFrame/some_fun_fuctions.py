import pandas as pd

movies = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\ratings.csv')
# .sort_values(['year','score'],ascending=False)
print(movies.columns)
# print(movies.sort_values(['IMDb Rating','Year'],ascending=False))
print(movies[['Directors','IMDb Rating','Year']].sort_values(['Year','IMDb Rating'],ascending=False))
print(movies[['Directors','IMDb Rating','Year']].sort_values(['Year','IMDb Rating'],ascending=False).drop_duplicates(subset='Year'))