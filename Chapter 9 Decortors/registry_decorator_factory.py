registry = set()

def register(active=True):
    def decorate(func):
        print('running register'
              f'(active={active}->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('funning f2()')

def f3():
    print('running f3()')

# import registration