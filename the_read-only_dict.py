from types import MappingProxyType
d = {'a':1}
d_proxy = MappingProxyType(d)
print(d_proxy['a'])
# d_proxy['b'] = 2 #wrong
d['b'] = 2
print(d_proxy)