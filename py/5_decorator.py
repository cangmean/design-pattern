"""
装饰器模式
"""

def cached(fn):
    _cache = dict()

    def _deco(*args):
        if args not in _cache:
            _cache[args] = fn(*args)
        return _cache[args]
    return _deco


@cached
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)