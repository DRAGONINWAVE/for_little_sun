import pandas as pd
import numpy as np



humid = pd.read_excel('C:\\Users\Administrator\Desktop\humid.xlsx')
semi_humid = pd.read_excel('C:\\Users\Administrator\Desktop\semi-humid.xlsx')
semi_arid = pd.read_excel('C:\\Users\Administrator\Desktop\semi-arid.xlsx')

# print(humid)
# RMSE =
EF1 = 1 - sum((humid.ET0_PMT_G-humid.ET0_PMT)**2)/sum((humid.ET0_PMT_G-np.average(humid.ET0_PMT))**2)
print(humid.ET0_PMT_G-humid.ET0_PMT,np.power(humid.ET0_PMT_G-humid.ET0_PMT,2),humid.ET0_PMT-np.average(humid.ET0_PMT))