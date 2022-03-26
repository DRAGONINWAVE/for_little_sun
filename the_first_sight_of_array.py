import numpy as np
a = np.arange(15)
a.shape = 3,5
print(a)
a = a.transpose() #swap rows and columns
print(a)