from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')


def top(series:Iterable[T],length:int) -> list[T]:
    ordered =sorted(series,reverse=True)
    return ordered[:length]

print(top([4,1,5,2,6,7,3],3))

l = 'mango pear apple kiwi banana'.split()
print(top(l,3))

l2 = [(len(s),s) for s in l]
print(l2)