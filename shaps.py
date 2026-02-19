while True:
    print("what size do you want to make your squear type one to exit ")
    choice = int(input())
    if choice == 1: 
        break
    
    for i in range(1 , choice + 1):
        for b in range(1 , choice + 1):
            print("*", end = "")
        print(" ")