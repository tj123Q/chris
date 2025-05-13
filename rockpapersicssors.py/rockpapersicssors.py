import random 
player_score = 0
computer_score = 0

games = 0
playing = True

while playing:
    choice = input("what is your choice?rock , papper , sizers , quit ")
    computer_choice = random.randint(1 , 3) 
    if choice == "quit":
        playing = False
    elif choice == "rock" and computer_choice == 1:
        print("you chose rock and the coputer chose rock.It is a tie!")
       
    elif choice == "rock" and computer_choice == 2:
        print("you chose rock and the coputer chose papper.computer wins")
        computer_score += 1
    elif choice == "rock" and computer_choice == 3:
        print("you chose rock and the coputer chose sizers.player  wins")
        player_score += 1
      
    elif choice == "paper" and computer_choice == 1:
        print("you chose paper and the coputer chose rock.player wins")
        player_score += 1

    elif choice == "sizers" and computer_choice == 2:
        print("you chose sizers and the coputer chose paper.player  wins")
        player_score += 1
    elif choice == "sizers" and computer_choice == 3:
        print("you chose sizers and the coputer chose sizers.It is a tie")
    
    elif choice == "paper" and computer_choice == 2:
        print("you chose paper and the coputer chose paper.It is a tie")
        computer_score += 1
    elif choice == "paper" and computer_choice == 3:
        print("you chose paper and the coputer chose sizers.computer wins")
        computer_score += 1
    elif choice == "sizers" and computer_choice == 1:
        print("you chose sizers and the coputer chose rock.computer wins")
        computer_score += 1
    
    games += 1
print(" game is over. you played "  +  str(games)+ " you won " + str(player_score) + " computer won " + str(computer_score))        