people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


# def f(person):
#     return person["name"]
#
# def f(person):
#     return person["house"]


people.sort(key=lambda person: person["name"])
print(people)


numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9]


t = [(9, 'f'), (1, 'z'), (4, 'a')]
sorted_t = sorted(t, key=lambda x: x[1])
print(sorted_t)  # [(4, 'a'), (9, 'f'), (1, 'z')]


# maps
nums = [1, 2, 3]
cubes = list(map(lambda x: x ** 3, nums))
print(cubes)  # [1, 8, 27]

# reduce
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

# filter
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

