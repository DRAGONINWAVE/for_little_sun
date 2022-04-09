import typing
# from unittest import result


class City(typing.NamedTuple):
    content : str
    name : str
    country : str



cities = [City('Asia', 'Tokyo', 'JP'), City('Asia', 'Delhi', 'IN'), City('North America', 'Mexico City', 'MX'), City('North America', 'New York', 'US'), City('South America', 'São Paulo', 'BR')]
# print(cities)

def match_asain_cities():
    result = []
    for city in cities:
        if city.content == 'Asia':
            cc = city.country
            result.append(cc)
    return result
print(match_asain_cities())
