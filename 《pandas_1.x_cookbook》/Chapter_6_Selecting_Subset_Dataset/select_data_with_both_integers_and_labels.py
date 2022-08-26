import pandas as pd
college = pd.read_csv(
    r'D:\python3.10\Pandas-Cookbook-master\data\college.csv',
                      index_col='INSTNM'
)
print(college)

col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
print(
    col_start,col_end
)
print(
    college.iloc[:5,col_start:col_end]
)

rows_start = college.index[10]
rows_end   = college.index[15]

print(
    college.loc[rows_start:rows_end,'UGDS_WHITE':'UGDS_UNKN']
)
print(
    college.iloc[10:16].loc[:,'UGDS_WHITE':'UGDS_UNKN']
)