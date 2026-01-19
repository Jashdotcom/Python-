import random
print("-----NUMBER GUESSING GAME-----")

number = random.randint(1,100)
attempts=0

guess = int(input("Enter your guess (1,100) : "))

while True:
    if guess<0 or guess>100:
        print("That number is out of range!")
        guess = int(input("Enter your guess (1,100) : "))
    elif guess<number:
        print("Too Low!Try again")
        attempts+=1
        guess = int(input("Enter your guess (1,100) : "))
        
    elif guess>number:
        print("Too High!Try again")
        attempts+=1
        guess = int(input("Enter your guess (1,100) : "))

    else:
        print(f"\n🎉 YOU GUESSED IT!Number was {number}.\nAttempts = {attempts}")
        break
   
   


