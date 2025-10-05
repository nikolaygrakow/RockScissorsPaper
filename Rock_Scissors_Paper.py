import random

import colorama

rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

player_move = input('Choose [r]ock, [s]cissors or [p]aper: ')

if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    raise SystemExit('Invalid Input. Try again ...')

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = scissors
elif computer_random_number == 3:
    computer_move = paper


if (player_move == rock and computer_move == scissors) or \
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move == rock):
    print(colorama.Fore.BLUE + f"The computer chose '{computer_move}'")
    print(colorama.Fore.GREEN + "Congratulations, You Win!")
elif player_move == computer_move:
    print(colorama.Fore.BLUE + f"The computer chose '{computer_move}'")
    print(colorama.Fore.YELLOW + "Draw!")
else:
    print(colorama.Fore.BLUE + f"The computer chose '{computer_move}'")
    print(colorama.Fore.RED + "Sorry, You Lose!")
