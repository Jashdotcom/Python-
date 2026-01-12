item = input("What item would you like to buy ? : ")
price = float(input("What is the price of that item ? ($) : "))
quantity = int(input("What is the quantity of that item ? : "))
total = price * quantity 

print(f"You have bought {quantity} X {item}/s")
print(f"Your total = ${total}")

