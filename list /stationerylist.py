while True:
    School_Stationery = [
        ["chunky pencil","slim pencil","RSVP pens","jelly ink pens"],
        ["binded book","hard cover books","lab books","cash book"]
    ]

    School_lunch_list = [
        ["fried chicken and rice","brown stew chicken and rice"],
        ["fried dumplings and jerk chicken","soup"]
    ]

  
    print("\n--- STATIONERY MENU ---")
    for r in range(len(School_Stationery)):
        for c in range(len(School_Stationery[r])):
            print(f"Row {r}, Column {c} = {School_Stationery[r][c]}")

    row = int(input("Choose stationery row: "))
    col = int(input("Choose stationery column: "))

    print("You chose:", School_Stationery[row][col])

    
    want_lunch = input("\nDo you want lunch? (yes/no): ")

    if want_lunch.lower() == "yes":

        print("\n--- LUNCH MENU ---")
        for r in range(len(School_lunch_list)):
            for c in range(len(School_lunch_list[r])):
                print(f"Row {r}, Column {c} = {School_lunch_list[r][c]}")

        lunch_row = int(input("Choose lunch row: "))
        lunch_col = int(input("Choose lunch column: "))

        print("You chose:", School_lunch_list[lunch_row][lunch_col])

    else:
        print("No lunch selected.")