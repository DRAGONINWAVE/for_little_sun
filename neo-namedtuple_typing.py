#added a type annotation
import typing
Coordinate = typing.NamedTuple('Coordinate',[('lat',float),('lon',float)])
print(Coordinate,tuple)
print(typing.get_type_hints(Coordinate))