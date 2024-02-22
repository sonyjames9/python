from curses.ascii import isalpha
import pandas

data = pandas.read_csv("py_100_days/python/100DaysCode/day30/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry only letters in alphabet")
    generate_phonetic()
  else:
    print(output_list)

generate_phonetic()