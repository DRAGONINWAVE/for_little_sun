from functools import reduce
from operator import add

print(reduce(add,range(100))) #4950
print(sum(range(100))) #4950