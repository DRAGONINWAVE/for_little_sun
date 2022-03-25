from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))
# print(floats)
fp = open('floats.bin','wb') #bin means binary
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7) #read 10million numbers from binary files
fp.close()
if floats == floats2:
    print('True')
