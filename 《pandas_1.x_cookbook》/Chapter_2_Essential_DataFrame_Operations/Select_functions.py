import pandas as pd
import numpy as np

movies = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\ratings.csv')
# print(movies.columns)
# print(movies.select_dtypes(include=int).head())
print(movies.select_dtypes(include=['number','float','object']).head())