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
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
avg(10)
print(avg(11))