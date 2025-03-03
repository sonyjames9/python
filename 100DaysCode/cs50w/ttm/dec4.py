import functools


@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# using custom cache with entire code for fibonacci
# def fibonacci(n, cache={}):
#     if n in cache:
#         return cache[n]
#
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
#
#     return cache[n]


print(fibonacci(40))