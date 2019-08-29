'''
This program will tell you the exact amount of coins you need in order to
save all money while paying back the customer. This is called the greedy program.
This code was written by Julian.
'''
while True:
    try:
        changeAmount = float(input("How much change is owed? ($)"))
        if changeAmount<0:
            print("Please put a positive number.")
            continue
        break
    except ValueError:
        print("That's not a valid input")
changeAmount = round(changeAmount * 100)
amountOfQuarters = (changeAmount // 25)
changeAmount = (changeAmount % 25)
print("You Need:",amountOfQuarters,"Quarter(s)")
amountOfDimes = (changeAmount // 10)
changeAmount = (changeAmount % 10)
print("You Need:",amountOfDimes,"Dime(s)")
amountOfNickels = (changeAmount // 5)
changeAmount = (changeAmount % 5)
print("You Need:",amountOfNickels,"Nickel(s)")
amountOfPennies = (changeAmount // 1)
print("You Need:",amountOfPennies,"Penny(ies)")
print("You Need",amountOfQuarters + amountOfDimes + amountOfNickels + amountOfPennies,"Coins.")
