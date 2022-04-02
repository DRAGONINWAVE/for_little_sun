#Example 5-4. Defining and using a named tuple type
from collections import namedtuple
City = namedtuple('City','country poplutation Coordinate')
Japanes = City('Japan',33.6,(23,32))
print(Japanes)  #name='Japan',poplutation='33.6',Coordinate=(23,32)
print(Japanes.country) #Japan
print(Japanes[1]) #33.6

print(City._fields) #show all the City fields
delhi_data = ('IN',77,(33,31))
delhi = City._make(delhi_data)
print(delhi) #City(country='IN', poplutation=77, Coordinate=(33, 31))
print(delhi._asdict()) #OrderedDict([('country', 'IN'), ('poplutation', 77), ('Coordinate', (33, 31))])
import json
print(json.dumps(delhi._asdict())) #{"country": "IN", "poplutation": 77, "Coordinate": [33, 31]}
Coordinate = namedtuple('Coordinate','lat lon reference',defaults=['WGS1984'])
print(Coordinate(0,0)) #Coordinate(lat=0, lon=0, reference='WGS1984')
print(Coordinate._field_defaults) #{'reference': 'WGS1984'}