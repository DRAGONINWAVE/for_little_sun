# class Averager():
#
#     def __init__(self):
#         self.series = []
#
#     def __call__(self,new_value):
#         self.series.append(new_value)
#         total = sum(self.series)
#         return total / len(self.series)
#
#
# ave = Averager()
# ave(10)
# print(ave(11))

#advanced way
# def make_averager():
#     series = []
#
#     def averager(new_value):
#         series.append(new_value)
#         total = sum(series)
#         return total / len(series)
#
#     return averager
#
#
# avg = make_averager()
# avg(10)
# print(avg(11),avg.__code__.co_freevars,avg.__closure__[0].cell_contents)
#



#Calculate a running average without keeping all history (fixed with the use of nonlocal)
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return  total/count

    return averager

avg = make_averager()
avg(10)
print(avg(11),avg.__code__.co_freevars,avg.__closure__[0].cell_contents)





