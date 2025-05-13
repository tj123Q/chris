"""
"hellow world"
print("hellow world")
name = ("christian")
age =15
color = ("yellow")
print(name , age , color)
"""

player1_username = input("Please enter Player 1's username: ")
player2_username = input("Please enter Player 2's username: ")

confirm_player1 = input("Please confirm Player 1's username: ")
if confirm_player1 != player1_username:
    print("Player 1: Username is wrong, it is not your username.")
else:
    print("Player 1: Username is correct, it is your username.")

confirm_player2 = input("Please confirm Player 2's username: ")
if confirm_player2 != player2_username:
    print("Player 2: Username is wrong, it is not your username.")
else:
    print("Player 2: Username is correct, it is your username.")

print("Player 1:", player1_username)
print("Player 2:", player2_username)


