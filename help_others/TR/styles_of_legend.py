import matplotlib.lines as mlines
import matplotlib.pyplot as plt
# import pandas as pd
# vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')

fig, ax = plt.subplots()

blue_line = mlines.Line2D([],
                          [],
                          # color='blue',
                          in_layout = True,
                          marker='*',
                          markerfacecolor='b',
                          markersize=15,
                          label='Blue stars',
                          markeredgecolor='r',
                          )
ax.legend(handles=[blue_line])
plt.show()