def fun(a,b,c,d,*rest):
    return a,b,c,d,rest
for i in range(4,7):#sry I forget the use of range
    print(i)
print(fun([1,2],2,3,*range(4,7)))
print(fun(*[1,2],2,3,*range(4,7)))