"""def sumfuc():
    a=5
    b=6
    sum=a+b
    print(sum)
sumfuc()


def name():
    print("Rana")


name()
name()
name()

def average(a,b):
    average=(a+b)/2
    print(average)
average(5,10)

def show_age(name="raza",age=7):
    print(f"{name} is age is {age}")

show_age("hassnain",17)
show_age()
 
def table_generator():
    a = int(input("Enter a number to generate its multiplication table: "))
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")


table_generator()

def sum(*number):
    total = 0
    for num in number:
        total += num
    return f"The sum is: {total}"

sum=sum(1,2,3,4,5,6,7,8,9,10)
print(sum) """

def is_even(number):
    return number % 2 == 0

# Loop chalega jab tak user stop na kare
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Program closed.")
        break
    
    # Input ko integer me convert karke check karna
    num = int(user_input)
    if is_even(num):
        print(f"{num} is even\n")
    else:
        print(f"{num} is odd\n")

def power():
    a = int(input("Enter the base number: "))
    b = int(input("Enter the exponent: "))
    result = a ** b
    return result
    
print("power is ",power())


def multiply(*multipliers):
    product = 1
    for multiplier in multipliers:
        product = multiplier * product
    return f"The product is: {product}"

multiply_result = multiply(1, 2, 3, 4, 5)
print(multiply_result)

def country(**country):
    for (key,value) in country.items():
        print(key,"-->",value)

country(name="Pakistan",capital="Islamabad",currency="Rupee")