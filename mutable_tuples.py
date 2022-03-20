# can judge it's immutable or not,return True meaming for immutable
def fixed(o):
    try :
        hash(o)
    except TypeError:
        return False and print('False')
    return True and print('True')

f1 = ('city','country',[1,2])
f2 = ('city','country',(1,2))

fixed(f1)
fixed(f2)

f1[-1].append(233)
print(f1)