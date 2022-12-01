# https: // pythonbasics.org/decorators/

import requests
from ast import arg
from time import perf_counter
import tracemalloc
from functools import wraps
from datetime import datetime
import sys
import time


def hello():  # type: ignore
  print("Hello")


message = hello

# Uncomment to check below decorator function
message()


def hello(func):
  def inner():
    print("Hello")
    func()
  return inner


@hello
def name():
  print("Alice")

# Uncomment to check below decorator function
# obj = hello(name)
# obj()
# name()


def dec_sum_ab(func):
  def inner(a, b):
    print(str(a) + " + "+str(b)+" is ", end="")
    return func(a, b)

  return inner


@dec_sum_ab
def sum_ab(a, b):
  res = a + b
  print(res)

# Uncomment to check below decorator function
# sum_ab(3, 4)


""" 
    Real world examples
    Use Case: Time measurement

"""


def measure_time(func):

  def wrapper(*arg):
    t = time.time()
    res = func(*arg)

    print("Function took " + str(time.time()-t) + " seconds to run")

    return res
  return wrapper


@measure_time
def my_func(n):  # type: ignore
  time.sleep(n)

# my_func(2)

# What is a Python Decorator
# The "decorators" we talk about with concern to Python are not exactly the same thing as the DecoratorPattern described above. A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well.


def simple_decorator(decorator):
    '''This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied.'''
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

#
# Sample Use:
#


@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        print(*args)
        print(**kwargs)
        return func(*args, **kwargs)
    return you_will_never_see_this_name


@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x


assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
# Uncomment to check below decorator function
# print(double(155))

"""
"""


def propget(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(func, prop.fset, prop.fdel, doc)
    return prop


def propset(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(prop.fget, func, prop.fdel, doc)
    return prop


def propdel(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, None, func, doc=func.__doc__)
    else:
        prop = property(prop.fget, prop.fset, func, prop.__doc__)
    return prop

# These can be used like this:


class Example(object):

    @propget
    def myattr(self):
        return self._half * 2

    @propset
    def myattr(self, value):
        self._half = value / 2

    @propdel
    def myattr(self):
        del self._half


# WHAT_TO_DEBUG = set(['io', 'core'])  # change to what you need


# class debug:
#     '''Decorator which helps to control what aspects of a program to debug
#     on per-function basis. Aspects are provided as list of arguments.
#     It DOESN'T slowdown functions which aren't supposed to be debugged.
#     '''

#     def __init__(self, aspects=None):
#         self.aspects = set(aspects)

#     def __call__(self, f):
#         if self.aspects & WHAT_TO_DEBUG:
#             def newf(*args, **kwds):
#                 print ( sys.stderr, f.func_name, args, kwds)
#                 f_result = f(*args, **kwds)
#                 print ( sys.stderr, f.func_name, "returned", f_result)
#                 return f_result
#             newf.__doc__ = f.__doc__
#             return newf
#         else:
#             return f


# @debug(['io'])
# def prn(x):
#     print (x)


# @debug(['core'])
# def mult(x, y):
#     return x * y


# prn(mult(2, 2))

# Read below examples when you want to revise decorators
# https: // python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html

# What Can You Do With Decorators?
# Decorators allow you to inject or modify code in functions or classes. Sounds a bit like Aspect-Oriented Programming(AOP) in Java, doesn’t it? Except that it’s both much simpler and (as a result) much more powerful. For example, suppose you’d like to do something at the entry and exit points of a function(such as perform some kind of security, tracing, locking, etc. – all the standard arguments for AOP). With decorators, it looks like this:

# Class as decorators
class entry_exit(object):  # type: ignore

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


@entry_exit
def func1():  # type: ignore
    print("inside func1()")


@entry_exit
def func2():  # type: ignore
    print("inside func2()")


func1()
func2()


print()

# Functions as decorators


def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    new_f.__name__ = f.__name__
    return new_f


@entry_exit
def func1():
    print("inside func1()")


@entry_exit
def func2():
    print("inside func2()")


func1()
func2()
print(func1.__name__+"\n")


# Python Decorators without arguments
class decorator_without_arguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")


@decorator_without_arguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call\n")
# Notice that __init__() is the only method called to perform decoration, and __call__() is called every time you call the decorated sayHello().


# Python Decorators with arguments.py
class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f


@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
# Now the process of decoration calls the constructor and then immediately invokes __call__(), which can only take a single argument (the function object) and must return the decorated function object that replaces the original. Notice that __call__() is now only invoked once, during decoration, and after that the decorated function that you return from __call__() is used for the actual calls.

# Although this behavior makes sense – the constructor is now used to capture the decorator arguments, but the object __call__() can no longer be used as the decorated function call, so you must instead use __call__() to perform the decoration – it is nonetheless surprising the first time you see it because it’s acting so much differently than the no-argument case, and you must code the decorator very differently from the no-argument case.


# Python Decorators_function_with_arguments
def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap


@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

print()

# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
# When to Use a Decorator in Python
# You'll use a decorator when you need to change the behavior of a function without modifying the function itself. A few good examples are when you want to add logging, test performance, perform caching, verify permissions, and so on.

# You can also use one when you need to run the same code on multiple functions. This avoids you writing duplicating code.


def log_datetime(func):
    """
    Log the date and time of a function 
    """

    def wrapper():
        print(
            f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()

    return wrapper


@log_datetime
def daily_backup():
    print('Daily backup job has finished\n')


print(daily_backup)
daily_backup()


def my_decorator_func(func):

    @wraps(func)
    # Functools wraps will update the decorator with the decorated functions attributes
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func


@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    pass


print(my_func.__name__)
print(my_func.__doc__)

print()


def measure_performance(func):
    """
    Measure performance of a function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current/10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak/10**6:.6f} MB')
        print(f'Time elapsed in seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    """Range"""
    my_list = list(range(100000))


@measure_performance
def make_list2():
    """List comprehension"""
    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    """Append"""
    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    """Concatenation"""

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


print(make_list1())
print(make_list2())
print(make_list3())
print(make_list4())


class LimitQuery:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used')
            return


@LimitQuery
def get_coint_price(limit):
    """
    View the bitcoin price index(BPI)
    """

    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


print(get_coint_price(5))
print(get_coint_price(5))
print(get_coint_price(5))
print(get_coint_price(5))
print(get_coint_price(5))
print(get_coint_price(5))

# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
