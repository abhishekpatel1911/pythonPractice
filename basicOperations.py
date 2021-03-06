# Basic Features:
# The aim of this program is to do basic math operation practice
# We can do the basic 4 operations. Addition, Subtraction, Multiplication, Division

# Advanced Features:
# ask for user input and create methods for the program
# ask the user if they want to perform another operation with the same numbers or different numbers

# @Author: Abhishek Patel


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
        user_choice = new_numbers()
        if user_choice == "2":
            continued
        elif user_choice is None:
            continued = False
    elif user_choice_to_continue == "N" or user_choice_to_continue == "n":
        continued = False
        print("Good bye")
    else:
        print("Please enter in a valid response!!")
        return choice_to_continue()  # Recursion
        continued = False

    return continued


def new_numbers():
    decision = True
    while decision:
        print("Do you want to perform another operation with the same numbers or different numbers")
        new_set_of_numbers = input("1. New Numbers, 2. Same Numbers")
        if new_set_of_numbers == "1":
            perform_operations()
            break
        elif new_set_of_numbers == "2":
            return new_set_of_numbers
        else:
            print("Please enter a valid choice")
            return new_numbers()


def menu_choice():  # This is the Menu that allows users to choose which operation they want to perform
    print("What operation would you like to perform:")
    menuChoice = input('1. Addition, 2. Subtraction, 3.Multiplication, 4. Division \n')
    if menuChoice == '1':
        return int(menuChoice)
    elif menuChoice == '2':
        return int(menuChoice)
    elif menuChoice == '3':
        return int(menuChoice)
    elif menuChoice == '4':
        return int(menuChoice)
    else:
        print("Please enter a valid choice")
        return menu_choice()


def perform_operations():  # Function to perform math operations based on choice made in the above function
    userInput1 = user_input_one()
    userInput2 = user_input_two()
    continued = True
    while continued:
        menuChoice = int(menu_choice())
        if menuChoice == 1:
            addition(userInput1, userInput2)
            continued = choice_to_continue()
        elif menuChoice == 2:
            subtraction(userInput1, userInput2)
            continued = choice_to_continue()
        elif menuChoice == 3:
            multiplication(userInput1, userInput2)
            continued = choice_to_continue()
        elif menuChoice == 4:
            division(userInput1, userInput2)
            continued = choice_to_continue()


def main():  # The driver of the code.
    print("********** Welcome to Basic Mathematics **********")
    print("Please enter in 2 numbers you would like to perform basic math operations with")
    perform_operations()


if __name__ == '__main__':
    main()
