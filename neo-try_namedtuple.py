from collections import namedtuple

Coordinate = namedtuple('Coordinate','lat lon')
print(issubclass(Coordinate,tuple))
moscow = Coordinate(233,666)
print(moscow)