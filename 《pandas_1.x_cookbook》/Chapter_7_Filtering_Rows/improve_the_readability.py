import pandas as pd
# from tushare import quotes

employee = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\employee.csv')

depts = [
    'Houston Police Department-HPD',
    'Houston Fire Department (HFD)'
]
select_columns = [
    'UNIQUE_ID',
    'DEPARTMENT',
    'GENDER',
    'BASE_SALARY'
]
qs = (
  'DEPARTMENT in @depts'
  " and GENDER == 'Female'"
  " and 80000 < = BASE_SALARY <= 120000"
)
emp_filtered = employee.query(qs)
print(
    emp_filtered[select_columns].head()
)
top10_depts = (
    employee.DEPARTMENT.value_counts().index[:10].tolist()
)
qs = "DEPARTMENT not in @top10_depts and GENDER == 'Female'"
employee_filtered2 = employee.query(qs)
print(
    employee_filtered2.head()
)