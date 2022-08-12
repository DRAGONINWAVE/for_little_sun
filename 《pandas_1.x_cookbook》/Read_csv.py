import pandas as pd

#pandas read csv file
movie = pd.read_csv(r'D:\迅雷下载\archive\IMDB Dataset.csv')
print(movie.columns)
print(movie.index)