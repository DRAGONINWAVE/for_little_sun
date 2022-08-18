import matplotlib.lines as mlines
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
blue_line = mlines.Line2D([], [], color='blue', marker='H',
                          markersize=15, label='Blue stars')
ax.legend(handles=[blue_line])

plt.show()