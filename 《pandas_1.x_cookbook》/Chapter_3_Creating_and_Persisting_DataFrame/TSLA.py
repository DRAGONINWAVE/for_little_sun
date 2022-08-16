import pandas as pd

tsla = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\TSLA.csv')

print(tsla.columns)

tsla_close  = tsla['Close']
tsla_cummax = tsla_close.cummax()
print(tsla_close.head(5))
print(tsla_cummax.head(5))