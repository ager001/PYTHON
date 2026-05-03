name = input("What is your name? ")
print(f"Welcome to the adventure, {name}!")

answer = input("You are on a path in a dark forest. Do you want to go left or right? (left/right) ")

if answer.lower() == "left":
    answer = input("You encounter a friendly elf who gives you  magical potion, which grants you the ability to fly, will you take it or leave it? (take/leave) ")
    if answer.lower() == "take":
        answer = input("You take the potion and gain the ability to fly! You soar through the sky and have an amazing adventure!")
    elif answer.lower() == "leave":
        print("You decide to leave the potion and continue on your path. You encounter a group of bandits who try to rob you, but you manage to escape!")
    
elif answer.lower() == "right" :
    print("You encounter a fierce dragon who breathes fire at you!")
else:
    print("Invalid choice. Please choose left or right.")


        