import pandas as pd
import matplotlib as plt
import os
import math
import numpy as np
from pandas import Series

names = os.listdir(r'D:\TD\my_work\data')
# print(names)

for name in names:
    print(name)
    ea = []
    df_raw = pd.read_excel('D:\TD\my_work\data\\'+name)
    k = 0
    es = []
    for AI in df_raw.AI:
        if AI >= 1.00:
            ea.append(float(0.611*math.exp(17.27*(df_raw.Tmean.values[k] - 2)/(df_raw.Tmean.values[k] - 2 + 273.3))))
        if 0.65<=AI<1:
            ea.append(float(0.611*math.exp(17.27*(df_raw.Tmin.values[k] - 0)/(df_raw.Tmin.values[k] - 0 + 273.3))))
        if 0.20<=AI<0.65:
            ea.append(float(0.611*math.exp(17.27*(df_raw.Tmin.values[k] - 1)/(df_raw.Tmin.values[k] - 1 + 273.3))))
        if 0.05<=AI<0.20:
            ea.append(float(0.611*math.exp(17.27*(df_raw.Tmin.values[k] - 2)/(df_raw.Tmin.values[k] - 2 + 273.3))))
        if AI<0.05:
            ea.append(float(0.611*math.exp(17.27*(df_raw.Tmin.values[k] - 4)/(df_raw.Tmin.values[k] - 4 + 273.3))))

    # print(len(Tdew))
        es.append((0.611*np.exp(17.27*df_raw.Tmin.values[k]/(df_raw.Tmin.values[k]+273.3))+0.611*np.exp(17.27*df_raw.Tmax.values[k]/(df_raw.Tmax.values[k]+273.3)))/2)
    # print(type(ea),type(es))
        k = k + 1

    df_raw.insert(df_raw.shape[1],'ea',ea)
    df_raw.insert(df_raw.shape[1],'es',es)
    VPD = df_raw.es - df_raw.ea
    df_raw.insert(df_raw.shape[1],'VPD',VPD)
    # kRs_G = []
    i = 0
    # for AI in df_raw.AI:
    kRs_G = (0.3648 - 0.0099*np.average(df_raw.Tmax.values - df_raw.Tmin.values) + 0.0194*np.average(df_raw.wind.values) - 0.0017*np.average(df_raw.RH.values))
        # i = i + 1
    # df_raw.insert(df_raw.shape[1],'kRs_G',kRs_G)
    print(kRs_G)
    # print(df_raw)
    # j = 0
    # # kRs_CF = []
    for AI in df_raw.AI:
        if AI >= 1.00:
            kRs_CF = (float(0.5191 - 0.0104*np.average(df_raw.Tmax.values - df_raw.Tmin.values)  + 0.0188*np.average(df_raw.wind.values) - 0.0035*np.average(df_raw.RH.values)))
        if 0.65<=AI<1:
            kRs_CF = (float(0.3958 - 0.0105*np.average(df_raw.Tmax.values - df_raw.Tmin.values) + 0.0186*np.average(df_raw.wind.values) - 0.0021*np.average(df_raw.RH.values)))
        if 0.20<=AI<0.65:
            kRs_CF = (float(0.3880 - 0.0095*np.average(df_raw.Tmax.values - df_raw.Tmin.values) + 0.0224*np.average(df_raw.wind.values)  - 0.0022*np.average(df_raw.RH.values)))
        if AI<0.20:
            kRs_CF = (float(0.2169 - 0.0042*np.average(df_raw.Tmax.values - df_raw.Tmin.values) + 0.0352*np.average(df_raw.wind.values) - 0.0011*np.average(df_raw.RH.values)))
        # j = j + 1
    # df_raw.insert(df_raw.shape[1],'kRs_CF',kRs_CF)
    print(kRs_CF,np.average(df_raw.wind.values),np.average(df_raw.AI.values))
    Rs_G = kRs_G*(df_raw.Tmax-df_raw.Tmin)**0.5*df_raw.Ra
    Rs_CF = kRs_CF*(df_raw.Tmax-df_raw.Tmin)**0.5*df_raw.Ra
    df_raw.insert(df_raw.shape[1],'Rs_G',Rs_G)
    df_raw.insert(df_raw.shape[1],'Rs_CF',Rs_CF)
    gamal = 1.013*10**(-3)/(0.662*2.45) * df_raw.Pa
    df_raw.insert(df_raw.shape[1],'gamal',gamal)
    delta = 4098*(0.6108*np.exp(17.27*df_raw.Tmean/(df_raw.Tmean+273.3)))/(df_raw.Tmean+273.3)**2
    df_raw.insert(df_raw.shape[1],'delta',delta)
    # print(df_raw)
    ET0_PMT_G = (0.408*df_raw.delta*df_raw.Rs_G + (df_raw.gamal*900/(df_raw.Tmean+273))*2*df_raw.VPD)/(df_raw.delta+df_raw.gamal*(1+0.34*2))
    ET0_PMT_CF = (0.408*df_raw.delta*df_raw.Rs_CF + (df_raw.gamal*900/(df_raw.Tmean+273))*2*df_raw.VPD)/(df_raw.delta+df_raw.gamal*(1+0.34*2))
    df_raw.insert(df_raw.shape[1],'ET0_PMT_G1',ET0_PMT_G)
    df_raw.insert(df_raw.shape[1],'ET0_PMT_CF1',ET0_PMT_CF)
    df_raw.to_excel('D:\TD\my_work\\data1\\' + name,index=False)