PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


with open('./Input/Names/invited_names.txt', 'r') as file:
    lines = file.readlines()

with open('./Output/output.txt', 'w') as file:
    for line in lines:
        reversed_line = ' '.join(word[::-1] for word in line.split())
        file.write(reversed_line + '\n')
