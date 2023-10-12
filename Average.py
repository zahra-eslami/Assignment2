Score_Sum=0
Score_Number=0
Score_Average=0
End= 0

Name=input ("Please Enter Your Name & Family , You Can Write end for Exit: ")
if Name=="end":
    End=1
while True and End==0:
    Score=input("Enter Your First Score:")
    if Score=="end":
        break
    else:
        Score_Sum =Score_Sum+ float(Score)
        Score_Number+=1

#print (f"{Score_Number} Score,\t{Score_Sum}")
if End==1:
    print("Dear You Haven't Enter Any Score, Good Luck")
else:
    Score_Average=round(Score_Sum/Score_Number,2) 
    if(Score_Average >= 17):
        print (f"Dear {Name} Your Average Is {Score_Average} \nThat's Great ")

    elif (17 > Score_Average >= 12):
        print (f"Dear {Name} Your Average Is {Score_Average} Acceptable \nYou Should Try More")

    elif (Score_Average < 12):
        print (f"Dear {Name} Your Average Is {Score_Average} \nSorry But You Have Failed, Try Harder")
