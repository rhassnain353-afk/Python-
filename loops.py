i = 1
while i<=10:
    print("Rana")
    i+=1


a = 5
b = 1
while a<=50 and b<=10:
    print("5 *", b, "=", a)
    a+=5
    b+=1

a = int(input("Enter a number for table  "))
b = 1
while b<=10 and a<=30:
    print(a, "*", b, "=", a*b)
    b+=1

i = 10
while i>=1:
    print(i)
    i-=1  

a = 1
while  a<=50:
  if a<=50and a%2==0:
    print(a,"Even number")
  else:
    print(a,"Odd number")
  a+=1
 

stored_numbers=[]
b = 5
while b>0:
   a = input("Enter your  number  ")
   stored_numbers.append(a)
   b -= 1
    