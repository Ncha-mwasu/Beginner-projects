#!/usr/bin/python3
from random import choice, sample
print("A game of Rock, Paper and Scissors")
print("Possible game plays are 'Rock', 'Paper', 'Scissors', 'end' to end the game\n")
user_score = 0
computer_score = 0
while True:
    
    plays = ["rock", "paper", "scissors"]
    user_play = str(input("Insert play: ").lower())
    game_plays = sample(plays, 1)
    computer_play = ''.join(game_plays)
    
    if (user_play != "rock" and user_play != "paper" and user_play != "scissors" and user_play != "end"):
        print("Please make a proper entry. Try again!\n")
        continue
    
    elif user_play == 'end':
        print("Game over\n")
        if user_score > computer_score:
            print(f"You win\n Your score: {user_score} Computer score: {computer_score}")
        elif user_score < computer_score:
            print(f"Computer wins\nYour score: {user_score} Computer score: {computer_score}")
        else:
            print(f"It's a tie\n Your score: {user_score} Computer score: {computer_score}")
        break
        
    elif computer_play == user_play:
        print(f"Computer play: {computer_play}")
        print("\nIt's a tie")
        computer_score = computer_score
        user_score = user_score
        
    elif computer_play == "paper":
        print(f"Computer play: {computer_play}")
        if user_play == "scissors":
            print("Victory! You win")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    
    elif computer_play == "scissors":
        print(f"Computer play: {computer_play}")
        if user_play == "rock":
            print("Victory! You win")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
            
    elif computer_play == "rock":
        print(f"Computer play: {computer_play}")
        if user_play == "paper":
            print("Victory! You win")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    
    score_user = user_score
    score_computer = computer_score
    
    print(f"\nComputer score: {score_computer}\nYour score: {score_user}")
    print()

