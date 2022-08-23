import pandas as pd
import numpy as np

college = pd.read_csv(r'D:\TD\《pandas_1.x_cookbook》\Pandas-Cookbook-master\data\college.csv',
                      index_col="INSTNM")


print(
    college.iloc[:3,:4]
)

print(
    college.loc[:'Amridge University',:'MENONLY']
)

print(
    college.iloc[:,[4,6]].head()
)

print(
    college.iloc[[100,200],[7,15]]
)

rows = [
    'GateWay Community College',
    'American Baptist Seminary of the West'
]

columns = [
    'SATMTMID','UGDS_NHPI'
]

print(
    college.loc[
        rows,columns
    ]
)

print(
    college.iloc[5,-4]
)
print(
    college.loc['The University of Alabama','PCTFLOAN']
)

print(
    college.iloc[90:80:-2,5]
)

start = 'Empire Beauty School-Flagstaff'
stop  = 'Arizona State University-Tempe'
print(
college.loc[start:stop:-2,'RELAFFIL']
)