import pandas as pd
import time
path='D:\\CHB.csv'
data=pd.read_csv(path,index_col=0)  #读取数据
#将CHB列中缺失的数据线性插值
data['CHB']=round(data['CHB'].interpolate(method = 'linear', axis=0),1)
#将时间列转为时间格式
data['观测日期']=pd.to_datetime(data['观测日期'],format='%Y%m%d')
#将时间作为索引
data = data.set_index('观测日期')

#保留一位小数
format1=lambda x:"%.1f"%x

#按月进行平均值统计
dfM=data.resample('M').mean()
dfM[['平均气温','平均相对湿度','2M风速','CHB']]=dfM[['平均气温','平均相对湿度','2M风速','CHB']].applymap(format1)#保留一位小数
#保存月平均数据
dfM.to_csv('D:\\舒适指数月平均.csv',encoding='gbk')

#按年进行统计
dfY=data.resample('Y').mean()
dfY[['平均气温','平均相对湿度','2M风速','CHB']]=dfY[['平均气温','平均相对湿度','2M风速','CHB']].applymap(format1) #保留一位小数
#保存年平均数据
dfY.to_csv('D:\\舒适指数年平均.csv',encoding='gbk')

#按季进行统计
dfQ=data['1960-5':'2018-11'].resample('3M').mean()
dfQ[['平均气温','平均相对湿度','2M风速','CHB']]=dfQ[['平均气温','平均相对湿度','2M风速','CHB']].applymap(format1) #保留一位小数
dfQ.to_csv('D:\\舒适指数季平均.csv',encoding='gbk')
