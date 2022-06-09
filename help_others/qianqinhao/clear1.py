import pandas as pd

raw_data = pd.read_excel('D:\TD\help_others\qianqinhao\\56875站数据.xlsx')
cleared_data = raw_data.dropna()
cleared_data.to_excel('cleared_dropna.xlsx',index=False)
print(cleared_data)