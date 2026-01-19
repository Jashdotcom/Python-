cart=[]
prices=()
total=0

menu={"popcorn" : 1.00,
       "hotdog" : 2.00,
       "pretzel" : 2.00,
       "nachos" : 4.50,
       "soda" : 1.00,
       "water" : 1.00,
       "fries" : 4.00,
       "coke" : 3.00,
       "burger" : 8.00,
       "pizza" : 10.00}

print("---------------MENU---------------\n")
for key,value in menu.items():
       print(f"{key:10} : ${value}")

print("\n--------------------------------------------------")
while True:
       food = input("Select an item (q to quit) :  ").lower()
       if food=="q":
              break
       elif menu.get(food) is not None:
              cart.append(food)

print("--------------------YOUR ORDER--------------------")

for food in cart:
       total+=menu.get(food)
       print(food, end=" ")

print(f"\nYour Total : ${total}")
              
