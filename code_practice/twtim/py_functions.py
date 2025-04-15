# PRINT function
age = 33
name = "Sony"

print("My name is", name, "and my age is", age, "years old", sep="|")
# print(f"My name is {name} and my age is {age} years old", sep="|")


# printing on same line
print("hello world", end=" | ")
print("My name", name)

# HELP function
help(print)

# RANGE function
rng = range(10)
print(list(rng))
rng = range(3, 10)
print(list(rng))
rng = range(3, 10, 2)
print(list(rng))
rng = range(10, -10, -2)
print(list(rng))


# MAP function
strings = ["my", "hello", "world", "apple"]
lengths = map(len, strings)

# Iterable is printed
print(lengths)
print(list(lengths))


def add_s(string):
    return string + "s"


# without lambda
lengths = map(add_s, strings)
print(list(lengths))

# using lambda(anonymous) function instead of add_s function
edit_lambda = map(lambda x: x + "q", strings)
print(list(edit_lambda))


# FILTER
def longer_than_4(string):
    return len(string) > 4


strings = ["my", "hello", "world", "ironman", "superman"]
filtered = filter(longer_than_4, strings)
# using lambda for same line above

print(filtered)
print(list(filtered))

# using lambda for filter
filtered_lamda = filter(lambda x: len(x) > 4, strings)
print(filtered_lamda)
print(list(filtered_lamda))


# SORTED
people = [
    {"name": "John", "age": 30},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 31},
]

sorted_people = sorted(people, key=lambda person: person["name"])
print(sorted_people)
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

sorted_people_rev = sorted(people, key=lambda person: person["name"], reverse=True)
print(sorted_people)
sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people)

print("\n")
# ENUMERATE
# how to use enumerate? and without using how much code do you need to write?

tasks = ["Write report", "Read report", "Attend meeting", "Code Review", "User Story"]

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}. {task}")

print()
#  Using enumerate
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

print(list(enumerate(tasks)))


print()
# ZIP
names = ["Alice", "Bob", "Charlie", "Dave"]
ages = [45, 23, 35, 20]

for idx in range(min(len(names), len(names))):
    name = names[idx]
    age = ages[idx]
    print(f"{name} is {age} years old")

names = ["Alice", "Bob", "Charlie", "Dave", "Jay"]
ages = [45, 23, 35, 20]
gender = ["Female", "Male", "Male"]
print()
combined = list(zip(names, ages, gender))
print(combined)
for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender}")


# OPEN
file = open("100DaysCode\\twtim\\test.txt", "w")
file.write(f"{name} is {age} years old")
file.close()

# Use with instead of manually opening and closing the file
with open("100DaysCode\\twtim\\test.txt", "w") as file:
    file.write("test test test \n test")

# Use with instead of manually opening and closing the file
with open("100DaysCode\\twtim\\test.txt", "r") as file:
    text = file.read()
    print(text)

# Use with instead of manually opening and closing the file
with open("100DaysCode\\twtim\\test.txt", "a") as file:
    file.write("\n new docs")

# Use with instead of manually opening and closing the file
with open("100DaysCode\\twtim\\test.txt", "r") as file:
    text = file.readlines()
    print(text)
