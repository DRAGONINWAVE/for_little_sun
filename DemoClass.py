import typing
class Coordinate(typing.NamedTuple):
    lat:float
    lon:float

trash = Coordinate('Ni',None)
print(trash) #match the inout Coordinate(lat='Ni', lon=None)

class DemoPlainClass:
    a:float
    b:float = 1.1
    c='spam'

#print(DemoPlainClass.a) #False
print(DemoPlainClass.b) #1.1
print(DemoPlainClass.c) #spam

import typing

class DemoNTClass(typing.NamedTuple):
    a:int
    b:float=1.1
    c = 'spam'

print(DemoNTClass.__annotations__) #only the typed values show ## {'a': <class 'float'>, 'b': <class 'float'>}
print(DemoNTClass.c) #actually it lived ##spam
print(DemoNTClass.__doc__) #show attributes ##DemoNTClass(a, b)

nt = DemoNTClass(8)
print(nt.a,nt.b,nt.c) #define a nt nt=8  8 1.1 spam

from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a:int
    b:float = 1.1
    c = 'spam'

print(DemoDataClass.__annotations__)

dc = DemoDataClass(9)
print(dc.a)

dc.a = 10
print(dc.a)
dc.b = 'opps'
dc.c = 'whatever'
dc.z = 'secret stash'
print(dc.c)