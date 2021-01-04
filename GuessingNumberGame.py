import random
from random import randint

def intro():
	message = "Welcome to the Number Guessing Game"
	print(message, '\n           RULES')
	rules = {1:'You get 3 tries to guess the number the computer generated', 2:'Once you run out of Guesses, the number will be revealed',3:'Numbers will be generated between 1 & 1000'}
	for i in rules:
		print(i,':',rules[i])


def random():
	rand1 = randint(0, 1000)
	return rand1

		
def message():
 	print("Please enter another guess")
 	
 	
def userGuess():
	userGuess = input('Input your guess')
	return userGuess


def game(rand1):
	numOfGuess = 0
	userInput = userGuess()
	print(str(rand1))
	guessRight = True
	while guessRight:
		if userInput > str(rand1):
			print("Guess: ",str(numOfGuess))
			print("You Guessed ", str(userInput))
			print("Your guess is greater than the number")
			guessRight = False
			message()
			numOfGuess +=1
			game(rand1)
		elif userInput < str(rand1):
			print("Guess: ", str(numOfGuess))
			print("You Guessed ", str(userInput))
			print("Your guess is less than the number")
			guessRight = False
			message()
			numOfGuess +=1
			game(rand1)
		else:
			numOfGuess +=1
			print("Guess: ",str(numOfGuess))
			print("You Guessed the correct number")
			print("The Number was: ", str(rand1))
			guessRight = False
				
		
def main():
	intro()
	rand1 = random()
	game(rand1)
	
	

		
main()
