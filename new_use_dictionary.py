def dump(**kwargs):
    return kwargs

print(dump(x = 2,**{'y':3},**{'z':4}))
b = {'a':0,**{'x':1},'y':2,**{'z':3,'x':4}}
print(b)