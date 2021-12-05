""""
lists
"""
import random

# I learnt to access a nested list you have to access the row you want first then the element in the list.
# Think of each list in a nested list as a row
# Some people pass 13 meaning column 1 row 3.

# ===========================================================================================================

# Rock, Paper, Scissors game.
rock = r"""
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----" """
paper = r"""
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 """
scissors = r"""
\ /
 X
O O"""
game_images = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("it's a draw!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
