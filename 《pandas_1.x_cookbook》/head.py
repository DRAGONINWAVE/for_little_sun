import pandas as pd

movie = pd.read_csv(r'D:\迅雷下载\archive\IMDB Dataset.csv')

Sentiment = movie['sentiment']
Review = movie['review']

print(Review.head())
print(Review.sample(n=5, random_state=42))
print(Sentiment.value_counts())
print(Sentiment.size)
print(Sentiment.shape)
print(Sentiment.unique())