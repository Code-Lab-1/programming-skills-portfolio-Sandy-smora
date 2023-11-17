# check if number is divisible by 5
num=int(input("Enter number here: "))

Divi = num%10
if Divi%5==0:
    print ("This is divisible by 5")
else:
    print("This is not divisible by 5")