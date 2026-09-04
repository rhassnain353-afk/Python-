print("------ATM Machine-----")
n = int(input("Please Enter the card or Card Number: "))
if n== 1234:
    print("Welcome to ATM Machine")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    choice = int(input("Please select an option: "))
    balance = 1000  
    
    if choice == 1:
        print(f"Your current balance is: ${balance}")
    
    elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}. New balance is: ${balance}")
        else:
            print("Insufficient funds.")
    
    elif choice == 3:
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"You have deposited {deposit_amount}. New balance is: ${balance}")
    
    else:
        print("Invalid option selected.")   