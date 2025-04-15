import json
import random
import re
import string
from collections import Counter
from itertools import combinations


def find_max_product(lst):
    """find the maximum product of two elements in a list"""
    max_product = float('-inf')
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            max_product = max(max_product, lst[i] * lst[j])
    return max_product


print(find_max_product([2, 4, 12, -5, -100, 6, 12]))


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))


class Student:
    """Class and object based program"""

    def __init__(self, name, age, rollno, location):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.location = location

    def display(self):
        print(f"Student information: Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Location: {self.location}")


class Branch(Student):
    def __init__(self, name, age, rollno, location, department):
        super().__init__(name, age, rollno, location)
        self.department = department

    def show_dept(self):
        self.display()
        print(f'Department: {self.department}')


student = Branch("Alice", 21, 101, "Helsinki", "CS")
student.show_dept()


def find_most_frequent_element(lst):
    """Find the most frequently occurring element in a list"""
    counter = Counter(lst)
    return max(counter.items(), key=lambda x: x[1])


print(find_most_frequent_element([1, 2, 3, 2, 3, 2, 4, 5]))


def longest_common_substring(s1, s2):
    """Find the longest common substring between 2 strings"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    max_len, end_idx = 0, 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i

    return s1[end_idx - max_len:end_idx]


print(longest_common_substring("abcdefabdf", "abdf"))


def parse_json_and_sum_categories(json_input):
    data = json.loads(json_input)['data']
    category_sums = {}
    for item in data:
        category = item['attributes']['category']
        price = item['attributes']['price']
        category_sums[category] = category_sums.get(category, 0) + price
    return category_sums


json_data = '{"data": [{"id": "1", "attributes": {"name": "Product A", "price": 100, "category": "Electronics"}}, {"id": "2", "attributes": {"name": "Product B", "price": 200, "category": "Furniture"}}, {"id": "3", "attributes": {"name": "Product C", "price": 150, "category": "Electronics"}}]}'
print(parse_json_and_sum_categories(json_data))


def merge_sorted_lists(a, b):
    """Merge two sorted lists"""
    c = []
    while a and b:
        c.append(a.pop(0) if a[0] < b[0] else b.pop())
    return c + a + b


print(merge_sorted_lists([1, 56, 78, 79, 100], [0, 2, 88, 89]))


def get_subarray_with_sum(arr, expected_sum):
    """Find the first subarray with sum equals to s"""
    left, current_sum = 0, 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > expected_sum and left <= right:
            current_sum -= arr[left]
            left += 1
        if current_sum == expected_sum:
            return [left + 1, right + 1]
    return [-1]


print(get_subarray_with_sum([1, 2, 3, 7, 5], 12))


def generate_random_list(size, max_val=40):
    """Generate a list of random integers withing a range"""
    return [random.randint(1, max_val) for _ in range(size)]


print(generate_random_list(10))


def check_string_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


sample_text = "The quick brown fox jumps over the lazy dog"
print("Is pangram:", check_string_pangram(sample_text))


def check_string_pangram_with_regex(s):
    return len(set(re.findall(r'[a-z]', s.lower()))) == 26


print("Is pangram:", check_string_pangram_with_regex(sample_text))


def check_string_pangram_without_for_loop(s):
    return all(c in s.lower() for c in string.ascii_lowercase)


print("Is pangram:", check_string_pangram_without_for_loop(sample_text))


def search_word_and_their_count_in_file(filename):
    """Count occurrences of each word in a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
    return dict(Counter(words))



def get_occurrence_of_word_from_file(filename, word):
    """Get occurrence of a specific word from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
    return words.count(word.lower())


def get_nth_number(n):
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a


print(get_nth_number(10))


def flatten_list(nested_list):
    """Flatten a nested list"""
    return [item for sublist in nested_list for item in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]


print("Flattened list:", flatten_list([1, [2, [3, 4]], 5]))


def get_smallest_element_from_unsorted_list(lst):
    return min(lst) if lst else None


# 10 & 14. Generate a list of 10 random integers (1-40)
def generate_random_list():
    return [random.randint(1, 40) for _ in range(10)]


sample_list = generate_random_list()
print("Random list:", sample_list)
print("Smallest element:", get_smallest_element_from_unsorted_list(sample_list))


def get_required_sum_from_list_pair_items(out_list, expected_sum):
    return [pair for pair in combinations(out_list, 2) if sum(pair) == expected_sum]


print("Pairs summing to 10:", get_required_sum_from_list_pair_items(sample_list, 10))


def find_max_product(l1):
    if len(l1) < 2:
        return None
    sorted_list = sorted(l1, reverse=True)
    return sorted_list[0] * sorted_list[1]


print("Max product:", find_max_product(sample_list))


def get_transpose_matrix_l1(matrix):
    return list(map(list, zip(*matrix)))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Transpose:", get_transpose_matrix_l1(matrix))


def find_most_occuring_element_and_count_from_list(lst):
    return Counter(lst).most_common(1)[0] if lst else (None, 0)


print("Most occurring element:", find_most_occuring_element_and_count_from_list(sample_list))
