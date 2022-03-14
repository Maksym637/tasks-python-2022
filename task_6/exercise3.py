from functools import lru_cache

c = 1

def count(f):
    @lru_cache()
    def wrapper(*args):
        global c
        c = c + 1
        return f(*args)
    return wrapper


@count
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))