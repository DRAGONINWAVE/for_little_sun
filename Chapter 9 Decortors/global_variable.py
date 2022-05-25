b = 6
def f1(a):
    print(a)
    global b
    print(b)
    b = 10

f1(3)