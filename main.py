import random
import clear
from art import logo

EASY_CHANCES = 10
HARD_CHANCES = 5


def number_of_chances():
    user_chances = input("Write 'easy' for 10 chances or 'hard' for 5 chances: ")
    if user_chances == 'easy':
        return EASY_CHANCES
    else:
        return HARD_CHANCES


def start_game():
    clear.clear()
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    my_number = round(random.random() * 100)
    chances = number_of_chances()
    game_over = False
    while not game_over:
        user_number = int(input("Please select a number to guess: "))
        if user_number == my_number:
            game_over = True
            print(f"You got it! the number was {my_number}")
        elif user_number > my_number:
            print("Number too HIGH")
        elif my_number > user_number:
            print("Number too LOW")

        chances -= 1
        if chances == 0:
            game_over = True
            print(f"You lost!, the number was {my_number}")
        elif not game_over:
            print(f"Guess again, you have {chances} left")


play_again = True
while play_again:
    start_game()
    play = input("Do you want to play again 'y'/'n': ")
    if play == 'n':
        play_again = False

