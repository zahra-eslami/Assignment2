import random
print("Please Enter To Roll The Dice")
input(" 🎲 ")
Dice_Number=random.randint(1,6)
while True:
    if Dice_Number==6:
        print("Congratulations! You Got '6',Roll It Again")

        Dice_Number=random.randint(1,6)
    else:
        print(f"You Got {Dice_Number}")
        break