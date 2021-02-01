import random  # Importing the random module so computer can choose between Snake , Water and Gun.


def gameWin(comp, you):
# Defining a gamewin function to establish a competion between a computer and user
    # Defining the game's condition. If you don't know the exact game rules of the game please google it.
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


print("Comp turn : Snake(s) Water(w) or Gun(g)?")

random_no = random.randint(
    1, 3
)  # Taking the random module in action to begin the game from computer's side


if random_no == 1:
    comp = "s"
elif random_no == 2:
    comp = "w"
elif random_no == 3:
    comp = "g"

you = input("Your turn : Snake(s) Water(w) or Gun(g)?")

a = gameWin(comp, you)
if a == None:
    print("The game is tied")
elif a:
    print("HURRAY!! You won the game")
else:
    print("Oops! You loose the game")

print(f"You chose {you}")
print(f"Comp chose {comp}")
