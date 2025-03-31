import inspect

def test_gen():
    yield 10
    yield 20

g = test_gen()

print(inspect.getgeneratorstate(g))  # NEW
next(g)
print(inspect.getgeneratorstate(g))  # SUSPENDED
next(g)
print(inspect.getgeneratorstate(g))  # SUSPENDED
try:
    next(g)
except StopIteration:
    print(inspect.getgeneratorstate(g))  # CLOSED