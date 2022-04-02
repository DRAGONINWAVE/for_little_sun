# from typing import NamedTuple
#

#vurses the dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
# class Coordinate(NamedTuple):

    lat : float
    lon : float

    def __str__(self):
        we = 'E' if self.lon>=0  else 'W'
        ns = 'N' if self.lat>=0  else 'S'

        return f'{self.lat:.1f}°{we}  {self.lon:.1f}°{ns}'

moscow = Coordinate(23.23,32.32)
print(moscow)