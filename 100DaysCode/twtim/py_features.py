def func_args(a, b, *args, values=[], **kwargs):
    print(a, b, args, kwargs, values)


func_args("1", "a", 1, 2, 3, key=2, value=7, values=[5, 6, 7])


def function_caller(func, *args, **kwargs):
    return func(*args, **kwargs)


def add(a, b):
    return a + b


def pow(base=1, exp=1):
    return base**exp


result = function_caller(add, 5, 10)
print(result)

result = function_caller(pow, base=2, exp=5)
print(result)


# Using functions as first class citizens

funcs = [add, pow, add, add]
args = [[(1, 2), {}], [(), {"base": 5, "exp": 2}], [(5, 6), {}], [(3, 4), {}]]

for func, (args, kwargs) in zip(funcs, args):
    result = func(*args, **kwargs)
    print(result)
