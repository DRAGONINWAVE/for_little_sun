import time

DEFAULT_TIME = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

class clock:

    def __init__(self,fmt=DEFAULT_TIME):
        self.fmt = fmt

    def __call__(self,func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter()
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result
        return clocked