#IF else condition
m = int(input("Enter your marks:"))
if m>=20:
    print("Pass")
else:
    print("Fail")
    print("Try Again")

Age = int(input("Enter Your age :"))
if Age >=18:
    print("Eligible for vote")
else:
    print("Not Eligible for Vote")

#if elif condition
marks = int(input("Enter your marks:"))
if marks >=90:
    print("Your Grade is A")
elif marks >=75 and marks<=89:
    print("Your grade is B")
elif marks >=50 and marks<=74:
    print("Your Grade is C")
else:
    print("You Fail")
