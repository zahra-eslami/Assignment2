Fib_Number = int(input("Please Enter Number Of Fibo Series You Want To Calculate :"))
First_Number = 1
Next_Number = 0
print("Your Fibonacci Series Are" ,end=": ")
for i in range(Fib_Number):
    Fibo = First_Number+Next_Number
    First_Number = Next_Number
    Next_Number=Fibo
    print(Fibo,end="  ")