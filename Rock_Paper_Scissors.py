import random

computer_score = 0
user_score = 0
user_ch=""
computer_ch=""

print("We Are Playing Rock,Paper,Scissors : We Play for 3 Rounds")
print("Please Use r for Rock,p for Paper,s for Scissors")
for i in range (3):
    
    x = random.randint(1 , 3)
    if x == 1 :
        computer_choice = "r"
        computer_ch="🧱"
    if x == 2 :
        computer_choice = "p"
        computer_ch="📃"
    if x == 3 :
        computer_choice = "s"
        computer_ch="✂"

    user_choice = input("Please Enter Your Choices : ")

    if user_choice == "r" :
        user_ch="🧱"
    elif user_choice == "p":
        user_ch="📃"
    elif user_choice == "s" :
        user_ch="✂"
    else:
        print("Your Choice Is Not In The Choices; I Choose For You 😁")
        user_choice1=random.randint(1,3)
        if user_choice1==1:
            user_choice="r"
            user_ch="🧱"
        elif user_choice1==2:
            user_choice="p"
            user_ch="📃"
        else:
            user_choice="s"
            user_ch="✂"
    
    print ("💻 : " , computer_ch ) 
    print ("👧 : ", user_ch) 

    if computer_choice == "r" and user_choice == "r":
        print("It's A Tie")

    elif computer_choice == "r" and user_choice == "p":
        user_score +=1
        print("Your Win")

    elif computer_choice == "r" and user_choice == "s":
        computer_score += 1
        print('Computer Win')

    elif computer_choice == "p" and user_choice == "p":
        print("It's A Tie")

    elif computer_choice == "p" and user_choice == "r":
        computer_score +=1
        print('Computer Win')

    elif computer_choice =="p" and user_choice == "s":
        user_score += 1
        print("Your Win")

    elif computer_choice == "s" and user_choice == "s":
        print("It's A Tie")

    elif computer_choice == "s" and user_choice == "r":
        user_score +=1
        print("Your Win")

    elif computer_choice =="s" and user_choice == "p":
        computer_score += 1
        print('Computer Win')

print("\nComputer score is :", computer_score) 
print("User score is ", user_score)
if computer_score>user_score:
    print("\nSorry, You Lost The Game")
elif computer_score<user_score:
    print("\nCongratulation, You Win The Game")
else:
    print("\nIt's A Tie")