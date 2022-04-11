a = [1,2,3,4]
b = a
print(b)
a.append(5)
print(b)

class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')

x = Gizmo()
print(x)
# y = Gizmo()*10
y = x
print(y) #It's  same

alex = {'name':'Charles L. Dodgson','born':1832,'balance':950}
charles = {'name':'Charles L. Dodgson','born':1832,'balance':950}
print(alex == charles)
print(alex is not charles)