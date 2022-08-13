import pandas as pd

# .rename
movies = pd.read_csv('ratings.csv')
# print(movies.columns)
col = {'Directors':'directors'}
movies = movies.rename(columns=col)
# print(movies.columns)

ids = movies.index.to_list()
# print(ids)
columns = movies.columns.to_list()
# print(columns)

# add a column,method 1
movies['has_seen'] = 0
print(movies)
# add a column,method 2
print(movies.assign(has_seen1=0))