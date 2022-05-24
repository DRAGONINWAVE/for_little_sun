from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar
from  collections import Counter
NumberT = TypeVar('NumberT',float,Decimal,Fraction,str)

def mode(data:Iterable[NumberT]) -> NumberT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


print(mode(["red","blue","blue","red","green","red","red"]))

