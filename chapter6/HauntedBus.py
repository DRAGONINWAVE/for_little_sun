class HauntedBus:

    def __init__(self,passengers=[]):
        self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

bus1  = HauntedBus(['Alice', 'Bob'])
print(bus1.passengers)  #['Alice', 'Bob']
bus2 = HauntedBus()
print(bus2.passengers)  #[]
bus2.pick('Alice')
print(bus2.passengers)  #Alice
bus3 = HauntedBus()
print(bus3.passengers)  #Alice