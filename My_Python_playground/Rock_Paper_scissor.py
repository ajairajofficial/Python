import os
import random

items = ['rock', 'paper', 'scissor']
player = input("Enter your name:\n")
i = int(input(f"Hello {player}! How many chances you want in a game \n"))
print(f"\nHello {player}! Lets play a game")
your_score = 0
computer_score = 0

for i in range(i):
    player_choice = input("\nPress r for rock, p for paper and s for scissor\n")
    player_choice = player_choice.lower()
    if player_choice == 'r':
        player_choice = items[0]
    elif player_choice == 'p':
        player_choice = items[1]
    elif player_choice == 's':
        player_choice = items[2]
    else:
        print("invalid entry")
    computer_choice = random.choice(items)
    os.system("cls")
    print(f"{player} choice is {player_choice} and computer choice {computer_choice}")
    if player_choice == computer_choice:
        print("\nIts a tie\n")
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'rock' and computer_choice == 'scissor':
        print(f"\n{player} wins\n")
        your_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("\ncomputer wins\n")
        computer_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print(f"\n{player} wins\n")
        your_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'paper' and computer_choice == 'scissor':
        print("\ncomputer wins\n")
        computer_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'scissor' and computer_choice == 'paper':
        print(f"\n{player} wins\n")
        your_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    elif player_choice == 'scissor' and computer_choice == 'rock':
        print("\ncomputer wins\n")
        computer_score +=1
        print(f"your score is {your_score} and computer score is {computer_score}")
    
if your_score > computer_score:
    print(f"\n{player} wins the game yeeeeeeeeeee\n")
elif your_score<computer_score:
    print("\nOopss sorry, computer wins the game\n")

    





