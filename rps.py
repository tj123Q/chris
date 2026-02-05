from random import randint
player_wins = 0
computer_wins = 0 
tie_counter = 0 
while True:
    print("do you what to paly a game for fun? ")
    print("1. cotinue to game")
    print("2. veiw score")
    print("3. exit")
    
    choice = int(input("waht would you like to do? "))
    if choice == 1:
        computer =  randint(0,2)
        print(" waht number do you chose? ")
        player = int(input("choice 0 == rock , 1 == paper , 2 == sissors "))
        if computer == player:
            print(f'computer number = {computer}')
            print(f'player number = {player}')
            print("its a tie 😲")
            tie_counter += 1
         
        
    
        if player == 0 and computer == 1:
            print("computer wins🎉")
            print("palyer had rock ")
            print("computer had papper")
            computer_wins += 1
       
        if player == 0 and computer == 2:
            print("player had rock")
            print("computer had sissors")
            print("palyer wins🎉")    
            player_wins += 1

        if player == 1 and computer == 0:
            print("player had paper")
            print("computer had rock")
            print("player wins🎉")
            player_wins += 1
        
        if player ==  1 and computer == 2:
            print("player had paper ")
            print("computer had sissors")
            print("computer wins🎉")
            computer_wins += 1

        if player == 2 and computer ==  1:
            print("player had psissors")
            print("computer had paper")
            print("player wins🎉")
            player_wins += 1
        
        if player == 2 and computer == 0:
            print("player had sissors")
            print("computer had rock")
            print("computer  wins🎉")
            computer_wins += 1
    if choice == 2:
        print(f'player wins {player_wins}')
        print(f'computer wins {computer_wins}')
        print(f'tie {tie_counter}')
    if choice == 3:
            break