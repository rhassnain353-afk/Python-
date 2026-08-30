#Arithmetic Operators
a = 5 
b = 5
print(a+b)#addition
print(a-b)#sub
print(a//b)#division
print(a/b)#float division
print(a*b)#multiplication 
print(a**b)#power

#Comparison Operators
print(a==b)#True
print(a>b)#False
print(a>=b)#True
print(a<b)#False
print(a<=b)#True
print(a!=b)#False

#Logical Operators
user_age = 20
has_driver_license = True

print("----And Operator----")
if user_age >= 18 and has_driver_license:
    print("Result: You are allowed to drive.\n")
else:
    print("Result: You are NOT allowed to drive.\n")

is_weekend = False
is_holiday = True

print("--- Testing OR Operator ---")
if is_weekend or is_holiday:
    print("Result: Today is a day off!\n")
else:
    print("Result: Today is a regular working day.\n")

is_raining = False

print("--- Testing NOT Operator ---")
if not is_raining:
    print("Result: It is not raining. You can go outside!\n")
else:
    print("Result: It is raining. Stay indoors.\n")
