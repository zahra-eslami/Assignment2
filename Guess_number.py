import random
computer_number=random.randint(10,50)

print("I Choose A Number Between 10 to 50, Guess What? You Only Have 10 Choices")

for i in range(10):
    user_number=int(input("Enter Your Guess : "))
    i=i+1
    if(computer_number==user_number):
        print("You Win","With",i,"Guesses 👍")
        break
    elif(computer_number>user_number):
        print("Go Up ☝")
    else:
        print("Go Down 👇")
if i>=10:
    print("You Lost")
    print("The Right Number was=",computer_number)

