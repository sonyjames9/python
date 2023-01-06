from typing import Dict


hobbies = {
    "Steve": ['Yoga', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

# for k, v in hobbies:
#   print(v[0])


def test(hobby: str, hobbies: dict) -> list:
  list_of_person = []
  for person in hobbies:
    # print(hobbies[k])
    # hobby = hobbies[k]
    if hobby in hobbies[person]:
      list_of_person.append(person)
  return list_of_person
  # return None


print(test('abc', hobbies))
print(test('Yoga', hobbies))
