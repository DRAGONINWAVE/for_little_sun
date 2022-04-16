import random

class BingoCage:

    def __init__(self,items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:
            return self.__items.pop()  #pick up and not return
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(54))
print(bingo.pick())            # return a number
print(bingo(),callable(bingo))                 # return a number  True