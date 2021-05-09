import random
i=1
win = 0
lose = 0
draw = 0
while i<=10:
    list = ["s","w","g"]
    choice = random.choice(list)
    print(f"{i}=> Enter 's' for snake 'w' for water and 'g' for gun")
    user_choice = input()
    if user_choice == "s":
        if choice == "s":
            print("Game Draw")
            draw += 1
        elif choice == "w":
            print("You Won Computer Choses water")
            win += 1
        else:
            print("You lose! Computer Choses Gun")
            lose += 1
    elif user_choice == "w":
        if choice == "s":
            print("You lose! Computer Choses Snake")
            lose += 1
        elif choice == "w":
            print("Game Draw")
            draw += 1
        else:
            print("You Won Computer Choses Gun")
            win+=1
    elif user_choice == "g":
        if choice == "s":
            print("You Won Computer Choses Snake")
            win+=1
        elif choice == "w":
            print("You lose! Computer Choses water")
            lose+=1
        else:
            print("Game Draw")
            draw+=1
    i+=1

print(f"You Won {win} times and loses {lose} time and Drawn {draw} times")