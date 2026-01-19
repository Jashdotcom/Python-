keypad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))

for row in keypad:
    for num in row:
        print(num,end=" ")
    print()