import pandas as pd
college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
college2 = college.set_index('STABBR')
print(
    college2.index.is_monotonic
)
college3 = college2.sort_index()
print(
    college3.index.is_monotonic
)
college_unique =college.set_index('INSTNM')
print(
    college_unique.index.is_unique
)
print(
    college[college['INSTNM'] == 'Stanford University']
)
print(
    college_unique.loc['Stanford University']
)
print(
    college_unique.loc[['Stanford University']]
)
college.index = (
    college['CITY'] + ',' + college['STABBR']
)
college = college.sort_index()
print(
    college.head()
)
print(
    college.loc['Miami,FL'].head()
)