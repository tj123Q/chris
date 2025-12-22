while True:
    answer= input ("are you ready")
    if answer == "no":
        break
    print("sinmple calculater")
    num1 = int(input("enter first number "))
    num2 = int(input("enter second number"))
    print("chose an option")
    print(" 1 add")
    print(" 2 subtract")
    print(" 3 multiple")
    print(" 4 divide")
    choice = input("Enter choice (1/2/3/4): " )
    if choice == "1":
        print("Answer:", num1 + num2)
    elif choice == "2":
        print("Answer:", num1 - num2)
    elif choice == "3":
        print("Answer:", num1 * num2)
    elif choice == "4":
        print("Answer:", num1 / num2)


