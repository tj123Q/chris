from random import randint
player_wins = 0
cpmputer_wins = 0 
tie_player = 0 
while True:
    print("do you waht to paly a game for fun? ")
    print("1.cotinue to game")
    print("2. veiw score")
    print("2. exit")
    
    choice = int(input("waht would you like to do? "))
    if choice == 1:
        computer =  randint(0,2)
        print(" waht number do you chose? ")
        player = int(input("choice 0 == rock , 1 == paper , 2 == sissors"))
        if computer == player:
            print(f 'computer number = {computer}')
            print(f 'player number = {player}')
            print("its a tie!")
            tie_player += 1
         
        
    
        if computer == player:
            print("player wins🎉")
            player_wins += 1
            computer_lost += 1
       
        if computer == player:
            print(f 'computer number = {computer}')
            print(f 'player number = {player}')
            print("you lost💀")    
            player_lost += 1
            computer_wins += 1
    if choice == 2:
    
        if choice == 3:
            break