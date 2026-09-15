a = [1,2,3,4,5,6,7,8,9,10]
for index, value in enumerate(a):
    print(f"Index: {index}, Value: {value}")


fruits = ['apple', 'banana', 'cherry', 'date']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

vegetables = ['carrot', 'broccoli', 'spinach', 'pepper']
for index, vegetable in enumerate(vegetables):
    print(f"Index: {index}, Vegetable: {vegetable}")


double = lambda x: x * 2
print(double(5))  
a = int(input("Enter a value: "))
square = lambda x: x ** 2
print(square(a))

a = int(input("Enter a value: "))
cube = lambda x: x ** 3
print(cube(a))