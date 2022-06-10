import matplotlib.pyplot as plt
import numpy as np
# import math

# from dec.spectral import rho

x = np.linspace(0,2*np.pi,1000)
y = 1-np.sin(x)
plt.subplot(polar=True)
plt.plot(x,y,c='green')
plt.show()