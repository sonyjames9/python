input_pattern = ["a", "ab", "abcd"]
reversed_pattern = [word[::-1] for word in input_pattern]
print(reversed_pattern)  # ['a', 'ba', 'dcba']


def reverse_string(s):
    return s[::-1]

# Example Usage
print(reverse_string("hello"))  # Output: 'olleh'
