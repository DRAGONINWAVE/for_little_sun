import pandas as pd
# import timeit
college = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\college.csv')
print(
    college[college['STABBR'] == 'TX'].head()
)

college2 = college.set_index('STABBR')
print(
    college2.loc['TX'].head()
)

states = ['TX','CA','NY']
print(
    college[college['STABBR'].isin(states)]
)
print(
    college2.loc[states]
)

