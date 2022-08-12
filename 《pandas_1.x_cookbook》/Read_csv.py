import pandas as pd

#pandas read csv file
movie = pd.read_csv(r'D:\迅雷下载\archive\IMDB Dataset.csv')
print(movie.columns)
print(movie.index)
print(movie.dtypes)
print(movie.dtypes.value_counts)
print(movie.info)

# the movie['sentiment'] is same as the movie.sentiment
print(movie['sentiment'],movie.sentiment)

# the functions of loc and iloc
# loc
print('movie.loc',movie.loc[:,'sentiment'])
print('movie.iloc',movie.iloc[:,1])

#