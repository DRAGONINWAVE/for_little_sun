class Coordinate:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

# from coordinates import Coordinate
moscow = Coordinate(123,123)
location = Coordinate(123,123)
print(location == moscow)
print(moscow.lat == location.lat & moscow.lon == location.lon)

