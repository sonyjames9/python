# List Comprehensions

even_list = [x for x in range(11) if x % 2 == 0]
odd_list = [x for x in range(11) if x % 2 != 0]

print(even_list)
print(odd_list)

# Function to get a list that contains all items of l smaller than x

l = [10, 15, 4, 6, 20, 14, 13]
x = 15


def get_smaller(l, x):
  return [e for e in l if e < x]


print(get_smaller(l, x))


def get_even_odd(l):
  even_list = [x for x in l if x % 2 == 0]
  odd_list = [x for x in l if x % 2 != 0]
  return even_list, odd_list


even_odd_list = [10, 30, 4, 5, 7, 19, 18]
even, odd = get_even_odd(even_odd_list)
print(even)
print(odd)

s = "geeksforgeeks"
print([x for x in s if x in "aeiou"])

s2 = ["geeks", "ide", "courser", "ggg"]
print([x for x in s2 if x.startswith("g")])
print([x.upper() for x in s2 if x.startswith("g")])

print([x*2 for x in range(6)])

# SET COMPREHENSION
l = [10, 20, 4, 6, 8, 5, 7, 10, 9, 4]
set1 = {x for x in l if x % 2 == 0}
set2 = {x for x in l if x % 2 != 0}

print(set1)
print(set2)

# DICT COMPREHENSION

l1 = [1, 4, 5, 3, 2]
d1 = {x: x**3 for x in l1}
d2 = {x: f"ID{x}"for x in range(5)}

l2 = [101, 103, 102]
l3 = ["ggg", "prac", "python"]
d3 = {l2[i]: l3[i] for i in range(len(l2))}
d4 = dict(zip(l2, l3))
d5 = {v: k for (k, v) in d4.items()}

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
