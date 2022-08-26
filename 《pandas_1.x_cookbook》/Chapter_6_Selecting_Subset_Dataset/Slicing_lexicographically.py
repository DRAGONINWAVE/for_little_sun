import pandas as pd
import numpy as np

college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',
                      index_col="INSTNM")

college = college.sort_index()

print(
    college.loc['Sp':'Su']
)
college = college.sort_index(ascending=False)
print(
    college.index.is_monotonic_decreasing
)
print(
    college.loc['E':'B']
)
