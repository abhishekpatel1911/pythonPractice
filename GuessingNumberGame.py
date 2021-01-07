import random

def intro():
	welcome_message = "Welcome to the Number Guessing Game"
	print(welcome_message, '\n           RULES')
	rules = {1:'You get 3 tries to guess the number the computer generated', 2:'Once you run out of Guesses, the number will be revealed',3:'Numbers will be generated between 1 & 1000'}
	for i in rules:
		print(i,':',rules[i])


def random_number():
	rand1 = random.randint(0, 1000)
	return rand1

		
def message():
	print("Please enter another guess")
 	
 	
def user_guess():
	userGuess = input('Input your guess')
	valid = userGuess.isdigit()
	if userGuess.isdigit():
		if int(userGuess) > 1000 or int(userGuess) < 0:
			print("Please enter a number between 0 & 1000")
			return user_guess()
		return userGuess
	else:
		print("Please enter a number not a letter")
		return user_guess()
	return userGuess


def game(rand1):
	numOfGuess = 1
	userInput = user_guess()
	guessRight = True
	while guessRight and numOfGuess < 4:
		if int(userInput) > rand1:
			print("Guess: ",str(numOfGuess))
			print("You Guessed ", userInput)
			print("Your guess is greater than the number")
			guessRight = True
			numOfGuess +=1
			if numOfGuess == 4:
				print("You ran out of Guesses, the number was: ", str(rand1))
			else:
				message()
				userInput= user_guess()
		elif int(userInput) < rand1:
			print("Guess: ", str(numOfGuess))
			print("You Guessed ", userInput)
			print("Your guess is less than the number")
			guessRight = True
			numOfGuess +=1
			if numOfGuess == 4:
				print("You ran out of Guesses, the number was: ", str(rand1))
			else:
				message()
				userInput = user_guess()
		else:
			numOfGuess +=1
			print("Guess: ",str(numOfGuess))
			print("You Guessed the correct number")
			print("The Number was: ", str(rand1))
			guessRight = False

'''
def test():
	valid = input("enter a number")
	valid2 = valid.isdigit()
	if not valid2:
		print("Please enter a number not a letter")
		return test()

	return valid
'''
		
def main():
	intro()
	rand1 = random_number()
	game(rand1)
#	test()

		
main()
