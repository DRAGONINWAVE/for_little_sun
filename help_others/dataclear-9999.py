import pandas as pd
import numpy as np
import openpyxl
BF = pd.read_excel(r'D:\piles\JAN.influence_factors.xlsx',dtype=np.float)
CF = BF.replace(-9999,' ')
CF.to_excel(r'C:\Users\Administrator\Desktop\dataclear.xlsx',index=False)
