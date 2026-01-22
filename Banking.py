import math

Amount=0
balance=0

while(True):
    print("\n**********************************")
    print("              BANKING             ")
    print("**********************************")

    print("\n1. Show Balance" 
        "\n2. Deposit"
        "\n3. Withdraw"
        "\n4. Exit")
    print("\n-----------------------------------")

    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    print("-----------------------------------")

    if choice==1:
        print(f"Your Balance : ${balance}")

    elif choice == 2:
        try:
            Amount = float(input("Enter the amount to be deposited : $"))
            if Amount <= 0:
                print("Amount should be greater than zero!")
            else:
                balance += Amount
                print(f"${Amount} Deposited Successfully.")
        except ValueError:
            print("Invalid amount!")

    elif choice == 3:
        if balance == 0:
            print("You have $0 in your account!")
        else:
            try:
                With_Amount = float(input("Enter the amount to withdraw : $"))
                if With_Amount <= 0:
                    print("Amount should be greater than zero!")
                elif With_Amount > balance:
                    print("The amount you are trying to withdraw is more than balance.")
                else:
                    balance -= With_Amount
                    print(f"${With_Amount} withdrawn successfully")
            except ValueError:
                print("Invalid amount!")


    elif choice == 4:
        print("\nThank you for using the Banking System.")
        break





    
    
