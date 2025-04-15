def find_palindromes(text):
    words = text.split()
    return [word for word in words if word == word[::-1]]


print(find_palindromes("madam level radar hello world"))

text = "hello world"
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)


def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()


print_pyramid(5)

nums = [1, 1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 4]
nums = list(set(nums))
print(nums)


def rev_list(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1
    return l


print(rev_list([2, 3, 5, 10, 12, 19, 20, 22]))
print(rev_list([12, 35, 10, 12, 19, 20, 22]))


even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)
odd_list = [x for x in range(11) if x % 2 != 0]
print(odd_list)