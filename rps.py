from random import randint
player_wins = 0
cpmputer_wins = 0 
tie_counter = 0 
while True:
    print("do you waht to paly a game for fun? ")
    print("1.cotinue to game")
    print("2. veiw score")
    print("2. exit")
    
    choice = int(input("waht would you like to do? "))
    if choice == 1:
        computer =  randint(0,2)
        print(" waht number do you chose? ")
        user = int(input("choice 0 == rock , 1 == paper , 2 == sissors"))
        if computer == user:
            print("its a tie!")
            tie_counter += 1
    if choice == 2:
    
    if choice == 3:
        break