rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of colums : "))
symbol = input("Symbol you want to print : ")

print()
for x in range(0,rows):
    for y in range(0,cols):
        print(f"{symbol}",end=" ")
    print()
