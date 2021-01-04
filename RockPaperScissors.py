# Classic Game #1: Rock Paper Scissors
# Basic Features:
# Play a game of Rock Paper Scissors
# Keep Track of Win-Loss Record
# Rules: Rock crushes Scissors, Paper covers Rock, and Scissors cut Paper

# Advanced Features:
# Give the User the choice of Multi-player or vs AI

# @Author: Abhishek Patel

import random


def game_menu():
    print("Lets play ROCK,PAPER, SCISSORS!!!")
    print("Choose your game type:")
    game_type = input("1. PvP, 2. vs AI")
    if game_type == str(1):  # code a PvP function to handle this
        continued = True
        player1_win_count = 0
        player2_win_count = 0
        while continued:
            score_board = pvp_scoreboard(player1_win_count, player2_win_count)
            print("Player1 choose your weapon: ")
            player1_choice = player_choice()
            print("Player2 choose your weapon: ")
            player2_choice = player_choice()
            outcome = vs_player(player1_choice, player2_choice)
            if outcome == "Player2":
                player2_win_count += 1
                continued = choice_to_continue()
            elif outcome == "Player":
                player1_win_count += 1
                continued = choice_to_continue()
            else:
                player2_win_count
                player1_win_count
                continued = choice_to_continue()
            if not continued:
                print("**********Final Score**********")
                print(score_board)
                print("*******************************")
                print("Good Game!! BYE!!")
    elif game_type == str(2):  # code a vs AI function to handle this
        continued = True
        player_win_count = 0
        ai_win_count = 0
        while continued:
            score_board = vs_ai_scoreboard(player_win_count, ai_win_count)
            print("Player choose your weapon: ")
            user_choice = player_choice()
            print("Computer choose your weapon: ")
            computer_choice = ai_choice()
            outcome = vs_ai(user_choice, computer_choice)
            if outcome == "Computer":
                ai_win_count += 1
                continued = choice_to_continue()
            elif outcome == "Player":
                player_win_count += 1
                continued = choice_to_continue()
            else:
                ai_win_count
                player_win_count
                continued = choice_to_continue()
            if not continued:
                print("Final Score: " + score_board)
                print("Good Game!! BYE!!")
    else:   # give a recursion call to the current method for an invalid input.
        print('Please enter in a valid choice')
        return game_menu()


def game_rules():
    print('******************** RULES ********************')
    print('1. Rock crushes Scissors'
          '2. Paper covers Rock'
          '3. Scissors cut Paper')


def player_choice():
    user_weapon_choice = input('1.Rock, 2.Paper, 3.Scissors')
    if user_weapon_choice == '1':
        print("Player: Rock ")
    elif user_weapon_choice == '2':
        print("Player: Paper ")
    elif user_weapon_choice == '3':
        print("Player: Scissors ")
    else:
        print('Please choose a valid weapon')
        return player_choice()
    return int(user_weapon_choice)


def ai_choice():
    print('1.Rock, 2.Paper, 3.Scissors')
    computer_weapon_choice = random.randint(1, 3)
    if computer_weapon_choice == 1:
        print("Computer: Rock ")
    elif computer_weapon_choice == 2:
        print("Computer: Paper ")
    else:
        print("Computer: Scissors ")
    return int(computer_weapon_choice)


def vs_ai(user_weapon_choice, computer_weapon_choice):
    if user_weapon_choice == 1 and computer_weapon_choice == 2 or user_weapon_choice == 2 and computer_weapon_choice == 3 or user_weapon_choice == 3 and computer_weapon_choice == 1:
        print("Computer Wins")
        winner = "Computer"
    elif user_weapon_choice == 2 and computer_weapon_choice == 1 or user_weapon_choice == 3 and computer_weapon_choice == 2 or user_weapon_choice == 1 and computer_weapon_choice == 3:
        print("You Win!!")
        winner = "Player"
    else:
        print("It's a TIE!!!")
        winner = "Tie"
    return winner


def vs_player(player1_weapon_choice, player2_weapon_choice):
    if player1_weapon_choice == 1 and player2_weapon_choice == 2 or player1_weapon_choice == 2 and player2_weapon_choice == 3 or player1_weapon_choice == 3 and player2_weapon_choice == 1:
        print("Player2  Wins!!!!")
        winner = "Player2"
    elif player1_weapon_choice == 2 and player2_weapon_choice == 1 or player1_weapon_choice == 3 and player2_weapon_choice == 2 or player1_weapon_choice == 1 and player2_weapon_choice == 3:
        print("Player1  Wins!!")
        winner = "Player"
    else:
        print("It's a TIE!!!")
        winner = "Tie"
    return winner


def choice_to_continue():  # This method is called when the user is asked if they want to continue playing the game.
    continued = True
    user_choice_to_continue = input("Would you like to play again? Y/N \n")
    if user_choice_to_continue == "Y" or user_choice_to_continue == "y":
        continued
    elif user_choice_to_continue == "N" or user_choice_to_continue == "n":
        continued = False
    else:
        print("Please enter in a valid response!!")
        return choice_to_continue()
    return continued


def vs_ai_scoreboard(player_win_count, computer_win_count):
    print("******************** SCORE BOARD ********************")
    score_board = "Computer: " + str(computer_win_count) + "       Player: " + str(player_win_count)
    print(score_board)
    print("*****************************************************")
    return score_board


def pvp_scoreboard(player1_win_count, player2_win_count):
    print("******************** SCORE BOARD ********************")
    score_board = "Player1: " + str(player1_win_count) + "         Player2: " + str(player2_win_count)
    print(score_board)
    print("*****************************************************")
    return score_board


if __name__ == '__main__':
    game_menu()
