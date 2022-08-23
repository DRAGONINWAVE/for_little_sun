import pandas as pd
import numpy as np

college = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\Pandas-Cookbook-master\data\college.csv',index_col="INSTNM")
print(college.columns)
city = college['CITY']
print(city)
print(city['Alabama A & M University'])
print(city.loc['Alabama A & M University'])
print(city.iloc[0])
print(city[[
    'Alabama A & M University',
    'Alabama State University',
]])
print(
    city.iloc[[1,4]]
)
print(
    city[
        'Alabama A & M University':
        'Alabama State University'
    ]
)

alabama_mask = city.isin(['Birmingham','Montgomery'])
print(alabama_mask)
print(city[alabama_mask])
print(college.loc['Alabama A & M University','CITY'])
print(college.iloc[0,0])
print(college.loc['Alabama A & M University':'Alabama State University','CITY'])