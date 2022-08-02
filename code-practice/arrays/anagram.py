from re import S
from turtle import st


def anagram(string1, string2):
  string1 = string1.replace(' ', "").lower()
  string2 = string2.replace(' ', "").lower()

  if len(string1) != len(string2):
    return False

  counter = {}

  for ch in string1:
    if ch not in counter:
      counter[ch] = 1
    else:
      counter[ch] += 1

  for ch in string2:
    if ch in counter:
      counter[ch] -= 1
    else:
      return False

  for k in counter:
    if counter[k] != 0:
      return False

  return True


check_anagram = "Strings are anagram : "
print("{} : {}".format(check_anagram,
                       anagram('clint eastwood', 'old west action')))
print("{} : {}".format(check_anagram, anagram('dog', 'god')))
print("{} : {}".format(check_anagram, anagram('dag', 'god')))


def anagram2(string1, string2):
  # Strip all spaces from both strings
  string1 = string1.replace(' ', "")
  string2 = string2.replace(' ', "")

  # Total No of characters is 256
  no_of_chars = 256

  # create an array with value = 0 for all 256 characters
  chars_array = [0 for _ in range(no_of_chars)]

  # Compare the length, if not same then exit the program
  if len(string1) != len(string2):
    return False

  # loop the string and store the ordial value of each character
  # Increment the 0 value by 1 each time a character is found in String1
  # Dccrement the char value by 1 each time a character is found in String2
  for ctr in range(len(string1)):
    chars_array[ord(string1[ctr]) - ord('a')] += 1
    chars_array[ord(string2[ctr]) - ord('a')] -= 1

  # loop counter for the total 256 chars in chars_array
  # if any value is not equal to 0, then return False, that strings are not anagram
  for ctr in range(no_of_chars):
    if chars_array[ctr] != 0:
      return False

  # return True of the string has done above checks
  return True


print("{} : {}".format(check_anagram,
                       anagram2('clint eastwood', 'old west action')))
print("{} : {}".format(check_anagram, anagram2('dog', 'god')))
print("{} : {}".format(check_anagram, anagram2('dag', 'god')))
