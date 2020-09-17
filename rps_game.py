#! usr/bin/env python3

import random

def rock_winstate(computer_move):
    if computer_move == 'scissors':
        print("You win!")
    elif computer_move == 'rock':
        print("You tied.")
    else: 
        print(f"You lost to {computer_move}")

def paper_winstate(computer_move):
    if computer_move == 'rock':
        print("You win!")
    elif computer_move == 'paper':
        print("You tied.")
    else:
        print(f"You lost to {computer_move}")

def scissors_winstate(computer_move):
    if computer_move == 'paper':
        print("You win!")
    elif computer_move == 'scissors':
        print("You tied.")
    else:
        print(f"You lost to {computer_move}")


def main():
    moveset = ['rock','paper','scissors']
    while True:
        computer_move = random.choice(moveset)
        player_move = input("Rock, paper, or scissors? Enter 'quit' to exit\n")
             
        if player_move == 'rock':
            rock_winstate(computer_move)
        elif player_move == 'paper':
            paper_winstate(computer_move)
        elif player_move == 'scissors':
            scissors_winstate(computer_move)
        elif player_move == 'quit':
            break

if __name__ == '__main__':
    main()