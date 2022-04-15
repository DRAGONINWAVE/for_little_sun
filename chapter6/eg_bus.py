class Bus:

    def __init__(self,passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers=list(passengers)

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

import copy
bus1 = Bus(['Alice','Bill','Claire','David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1),id(bus2),id(bus3))
bus1.drop('Alice')
print(bus2.passengers,bus3.passengers)
a = [10,20]
b = [a,30]
a.append(b)
print(a)
bus2.drop('Bill')
bus2.pick('longyan')
bus4 = Bus()
print(bus4.passengers)
