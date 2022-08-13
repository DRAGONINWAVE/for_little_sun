import pandas as pd
import numpy as np

movies = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\ratings.csv')
print(movies.columns)
# print(movies.select_dtypes(include=int).head())
# print(movies.select_dtypes(include=['number','float','object']).head())

# filter and like=
# print(movies.filter(like='D').head())

col = ['URL','description']
# print(movies.filter(items=col).head())
# abbr. 正则表达式（regular expression）
# print(movies.filter(regex='d').head())
# print(movies.shape)
# print(movies.ndim)
# print(movies.count())
print(movies.describe(percentiles=[0.44,0.22,0.99]).T)
print(movies.min(skipna=False))
