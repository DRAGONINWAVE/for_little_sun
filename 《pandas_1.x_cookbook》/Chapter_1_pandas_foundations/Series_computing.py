import pandas as pd

money = pd.Series([100,20,None])
print(money - 15)
print(money.sub(15,fill_value=0))