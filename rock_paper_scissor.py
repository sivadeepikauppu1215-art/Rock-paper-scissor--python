#Rock, Paper and Scissor Game 

#importing required libraries
import random


game_rule = ['Rock','Paper','Scissor']
s = 'Continue'


while s!='End':
    user = input("Enter choice as Rock or Paper or Scissor\n")
    computer = random.choice(game_rule)
    
    if computer == user:
        print("Tie\n")
        
    elif user == 'Rock':
        if computer == "Paper":
            print("Computer Wins the Game\n")
        else:
            print("User Wins the Game\n")
            
    elif user == 'Paper':
        if computer == "Scissor":
            print("Computer Wins the Game\n")
        else:
            print("User Wins the Game\n")
            
    elif user == 'Scissor':
        if computer == "Rock":
            print("Computer Wins the Game\n")
        else:
            print("User Wins the Game\n")
            
    else:
        print("Please enter correct choice\n")
    s = input("Enter choice as Continue or End\n")