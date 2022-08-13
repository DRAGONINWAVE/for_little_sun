import pandas as pd

# .rename
from pandas import Index

movies = pd.read_csv('ratings.csv')
# print(movies.columns)
col = {'Directors': 'directors'}
print(type(col))
movies = movies.rename(columns=col)
# print(movies.columns)

ids = movies.index.to_list()
# print(ids)
columns = movies.columns.to_list()
# print(columns)

# add a column,method 1
movies['has_seen'] = 0
# print(movies)
# add a column,method 2
# print(movies.assign(has_seen1=0))

x = []
for c in movies.columns:
    x.append(c.lower())
print(x)
movies.columns = x
print(movies.columns)
