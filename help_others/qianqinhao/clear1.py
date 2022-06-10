import pandas as pd

raw_data = pd.read_excel('D:\TD\help_others\qianqinhao\\56875站数据.xlsx',sheet_name='降水')
raw_data1 = raw_data.drop(raw_data[raw_data['20-20时累计降水量']>30000].index)
cleared_data = raw_data1.dropna()
cleared_data.to_excel('P_cleared_dropna.xlsx',index=False)
print(cleared_data)