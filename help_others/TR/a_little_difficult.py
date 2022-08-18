import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
# Funky hack to change the number of "stars" in the legend to be 1,
# I feel like there has to be a better way to do this...
from pylab import *
rcParams['legend.numpoints'] = 1
vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')


corr = vehicle[["city08", "highway08", "cylinders"]].corr()
# x = np.r_[0.,3.15,5.39,7.29,11.55,14.4,19.8,23.4,25.7]
# y = np.r_[0,0.13,0.2,0.27,0.42, 0.51,0.68,0.80,0.88]
# model = linear_model.LinearRegression()
# X = x.reshape(-1,1)
# Y = y.reshape(-1,1)
# model.fit(X,Y)
x = vehicle['city08']
y1 = vehicle['highway08']
y2 = vehicle['cylinders']

green_line, = plt.plot(x,y1, marker='o',markersize=10,fillstyle='left')
blue_dot, = plt.plot(x,y2, marker='o',markersize=14,fillstyle='left')
plt.legend([(blue_dot, green_line)], ["DesiredKey"], loc='upper center')
plt.savefig('ugly_guy.png')