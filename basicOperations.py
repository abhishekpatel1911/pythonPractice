# Basic Features:
# The aim of this program is to do basic math operation practice
# We can do the basic 4 operations. Addition, Subtraction, Multiplication, Division

# Advanced Features:
# ask for user input and create methods for the program


def addition(input1, input2):  # Add Method
    print("You chose to add the numbers: " + input1 + " & " + input2 + "\n")
    sumTotal = int(input1) + int(input2)
    return print(input1 + " + " + input2 + " = " + str(sumTotal))


def subtraction(input1, input2):  # Subtract Method
    print("You chose to subtract the numbers" + input1 + " & " + input2 + "\n")
    diffTotal = int(input1) - int(input2)
    return print(input1 + " - " + input2 + " = " + str(diffTotal))



def multiplication(input1, input2):  # Multiply Method
    print("You chose to multiply the numbers" + input1 + " & " + input2 + "\n")
    multiplicationTotal = int(input1) * int(input2)
    return print(input1 + " * " + input2 + " = " + str(multiplicationTotal))


def division(input1, input2):  # Divide Method
    print("You chose to divide the numbers" + input1 + " & " + input2 + "\n")
    quotientTotal = int(input1) / int(input2)
    return print(input1 + " / " + input2 + " = " + str(quotientTotal))


def user_input_one():  # Takes the users first input
    user_choice_of_number = input("Enter in a number\n")
    return user_choice_of_number


def user_input_two():  # Takes the users second input
    user_choice_of_number = input("Enter in another number\n")
    return user_choice_of_number


def choice_to_continue():  # This method is called when the user is asked if they want to try a diff operation
    continued = True
    user_choice_to_continue = input("Would you like to perform another operation? Y/N \n")
    if user_choice_to_continue == "Y" or user_choice_to_continue == "y":
        continued
    elif user_choice_to_continue == "N" or user_choice_to_continue == "n":
        continued = False
        print("Good bye")
    else:
        print("Please enter in a valid response!!")
        choice_to_continue()
    return continued


def menu_choice():  # This is the Menu that allows users to choose which operation they want to perform
    print("What operation would you like to perform:")
    menuChoice = input('1. Addition, 2. Subtraction, 3.Multiplication, 4. Division \n')
    return menuChoice


def perform_operations():  # Function to perform math operations based on choice made in the above function
    continued = True
    while continued:
        userInput1 = user_input_one()
        userInput2 = user_input_two()
        menuChoice = menu_choice()
        if int(menuChoice) == 1:
            addition(userInput1, userInput2)
            continued = choice_to_continue()
        elif int(menuChoice) == 2:
            subtraction(userInput1, userInput2)
            continued = choice_to_continue()
        elif int(menuChoice) == 3:
            multiplication(userInput1, userInput2)
            continued = choice_to_continue()
        elif int(menuChoice) == 4:
            division(userInput1, userInput2)
            continued = choice_to_continue()
        else:
            print("Please enter in a valid choice")
            perform_operations()


def main():  # The driver of the code.
    print("********** Welcome to Basic Mathematics **********")
    print("Please enter in 2 numbers you would like to perform basic math operations with")
    perform_operations()


if __name__ == '__main__':
    main()
