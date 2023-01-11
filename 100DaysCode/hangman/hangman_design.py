# Step1
import random

# from code_practice.hangman.hangman_words import word_list
from hangman_words import word_list
from stages_art import stages, logo

# word_list = ['camel', 'baboon']

# TODO 1- Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# TODO-2: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)

#TODO: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

print(logo)

for _ in range(word_length):
	display += "_"
print(display)

#TODO: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
	print(f"Total lives : {lives}")
	# TODO-3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
	guess = input("Guess a letter : ").lower()

	# TODO-4 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
	if guess in display:
		print(f"You've already guessed {guess}")

	#TODO-5: - Loop through each position in the chosen_word;
	#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
	#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
	for position in range(word_length):
		letter = chosen_word[position]
		if letter == guess:
			display[position] = letter
	# TODO: - If guess is not a letter in the chosen_word,
	# Then reduce 'lives' by 1.
	# If lives goes down to 0 then the game should stop and it should print "You lose."
	if guess not in chosen_word:
		print(f"The guessed letter {guess} is not in the word, you lost a life")
		lives -= 1
	# TODO: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
		print(stages[lives])
		if lives == 0:
			end_of_game = True
			print("You lose")
			print(f"The right word is {chosen_word}")

	#TODO: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
	#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
	# Join all the elements in the list and turn it into a String.
	print(f"{' '.join(display)}")

	if "_" not in display:
		end_of_game = True
		print("You win")
