import pandas as pd
import numpy as np

college = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\Pandas-Cookbook-master\data\college.csv',
                      index_col="INSTNM")

print(
    college.sample(5,random_state=42)
)
print(
    college.iloc[20]
)

print(
    college.loc['University of Alaska Anchorage']
)
print(
    college.iloc[[60,99,3]]
)

print(
    college.iloc[[60,99,3]].index.tolist()
)