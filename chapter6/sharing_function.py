def f(a,b):
    a+=b
    return a

x = 1
y = 2
print(f(x,y))
print(x,y)
x = [1,2]
y = [2,3]
print(f(x,y))
print(x,y)
x = (1,3)
y = (2,4)
print(f(x,y))
print(x,y)