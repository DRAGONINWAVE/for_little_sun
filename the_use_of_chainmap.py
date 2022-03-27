import collections
from collections import ChainMap
d1 = {'a':1,'b':2,'c':3}
d2 = {'a':2,'b':3,'c':4,'d':5}
chain = ChainMap(d1, d2)
print(chain['a'])
chain['c'] = 233
print(chain)
import builtins
pylookup = ChainMap(locals(),globals(),vars(builtins))
# print(pylookup)
ct = collections.Counter('abracadabra')
print(ct)
print(ct.most_common(3))
