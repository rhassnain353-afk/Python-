email = "rana786687"
password = "rana786687"
print("---Wellcome to my Website---")
print("1. Login")
print("2.Sign up")
while True:
    a = int(input("Select option to contiune:"))
    if a==1:
        user_email = input("Enter your email: ")
        user_password = input("Enter your password: ")
        if user_email!=email:
            print("In Valid email,Try again")
            print(a)
        elif user_password!=password:
            print("Invaild Password")
        else:
            print("Login successful")
            break

    elif a==2:
        name = input("Enter name to sign up:")
        age = input("Enter your age :")
        birthday = input("Enter your birthday:")
        email= input("Enter email:")
        gender = input("Enter your Gender:")
        password = input("Enter the strong password:")
        user_information={"Name" :name,"Age":age,"Birthday":birthday,"Email":email,"Gender":gender,"Password":password}
        print("Your account has been created successfully")
        for key,value in user_information.items():
            print(key,":",value)
            break
        
    else:
        print("Invalid option, please select 1 or 2.")
       
        