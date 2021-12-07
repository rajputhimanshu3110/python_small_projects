import random
print("\t*****WELCOME TO NUMBER GUESSING GAME*****\n")
list = [93,52,55,165,28,17,65,954.326,454]
n = random.randrange(1,500)
chances = 9
print("Enter number b/w 1 to 500")
while (True):
    if(chances>0):
        number = int(input("Enter number : "))
        if number>n:
            print("guess lesser number")
            chances = chances -1
            print(f"Only {chances} chances left")
        elif number==n:
            chances = chances -1
            print(f"You won and takes {9-chances} chances")
            break
        else:
            print("Guess higher number")
            chances = chances -1
            print(f"Only {chances} chances left")
    else:
        print("You lose! Game Over")
        break
