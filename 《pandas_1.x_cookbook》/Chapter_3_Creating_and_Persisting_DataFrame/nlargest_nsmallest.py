import pandas as pd

movies = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\ratings.csv')
# print(movies[['Directors','IMDb Rating','Year']].nlargest(5,'IMDb Rating').nsmallest(10,'Year'))

print(movies[['Directors','IMDb Rating','Year']].nlargest(1000,'IMDb Rating').tail())