print("1. +")
print("2. -")
print("3. *")
print("4. /")

num = int(input("Enter operation number to perform (1,2,3,4) : "))
print("")
if num==5 :
    print("Enter a valid choice")
elif num==1 :
    num1 = float(input("Enter first number :  "))
    num2 = float(input("Enter second number : "))
    result = num1+num2
    print(f"{num1} + {num2} = {result}")
elif num==2 :
    num1 = float(input("Enter first number :  "))
    num2 = float(input("Enter second number : "))
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif num==3 :
    num1 = float(input("Enter first number :  "))
    num2 = float(input("Enter second number : "))
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif num==4 :
    num1 = float(input("Enter first number :  "))
    num2 = float(input("Enter second number : "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
    




 









