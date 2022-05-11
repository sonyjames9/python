"""
Create a count array of alphabet size which is typically 256. Initialize all values of count array as 0.
Traverse the given string and increment count of every character.
Traverse the count array and if the count array has more than one odd values, return false. Otherwise, return true.
"""


def palindrome_using_chars(palindrome_str):
    NO_OF_CHARS = 256

    # def can_form_palindrome(palindrome_str):
    count = [0] * NO_OF_CHARS

    for i in range(0, len(palindrome_str)):
        count[ord(palindrome_str[i])] = count[ord(palindrome_str[i])] + 1

    # Count odd chars, if the string has more than 1 odd char, then the string is not palindrome, return False
    # If sa
    odd = 0
    for i in range(0, NO_OF_CHARS):
        if count[i] & 1:
            odd = odd + 1

        if odd > 1:
            return False

    return True


palindrome_str = "geeksogeeks"
print(f'String {palindrome_str} is palindrome :  {palindrome_using_chars(palindrome_str)}')

palindrome_str = "geeksforgeeks"
print(f'String {palindrome_str} is palindrome : {palindrome_using_chars(palindrome_str)}')


def palindrome_using_list(palindrome_str):
    palindrome_list = []

    for ctr in range(len(palindrome_str)):
        if palindrome_str[ctr] in palindrome_list:
            palindrome_list.remove(palindrome_str[ctr])
        else:
            palindrome_list.append(palindrome_str[ctr])

    # if character length is even list is expected to be empty
    # or if character length is odd list size is expected to be 1
    if len(palindrome_str) % 2 == 0 and len(palindrome_list) == 0 or len(palindrome_str) % 2 == 1 and len(
            palindrome_list) == 1:
        return True
    else:
        return False


palindrome_str = "geeksogeeks"
print(f'String {palindrome_str} is palindrome :  {palindrome_using_list(palindrome_str)}')

palindrome_str = "geeksforgeeks"
print(f'String {palindrome_str} is palindrome : {palindrome_using_list(palindrome_str)}')


