import random

running = True
while (running):
    
    options = ("rock","paper","scissors")

    computer = random.choice(options)

    user = input("\nEnter your choice (rock,paper,scissors) : ").lower()

    print(f"\nComputer's choice : {computer}")
    print(f"Your choice : {user}")

    if computer=="rock" and user=="paper" or computer=="scissors" and user=="rock" or computer=="paper" and user=="scissors":
        print("\nYOU WON 🏆")
    elif computer=="paper" and user=="rock" or computer=="rock" and user=="scissors" or computer=="scissors" and user=="paper":
        print("\nYOU LOSE ❌")
    elif computer=="rock" and user=="rock" or computer=="paper" and user=="paper" or computer=="scissors" and user=="scissors":
        print("\nTIE 🤝")
    else:
        print(f'\nThere\'s no option of "{user}"!')

    print("-------------------------------------------------")
    play_again = input("Play Again ? (Y or N) : ").upper()
    print("-------------------------------------------------")

    if not play_again == "Y":
        running = False
        print("\nBye,Thanks for Playin'🙌🏼")






