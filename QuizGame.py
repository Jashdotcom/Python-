questions=("1. How many elements are there in the periodic table ?",
           "2. Which animal lays the largest eggs ? ",
           "3. What is the most abundant gas in Earth's atmosphere ?",
           "4. How many bones are in the human body ? ",
           "5. Which planet in the solar system is the hottest ?")

options=(("A. 116", "B. 117", "C. 118", "D. 119"),
         ("A. Whale", "B. Crocodile" ,"C. Elephant" ,"D. Ostrich"),
         ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
         ("A. 206", "B. 207", "C. 208", "D. 209"),
         ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

Answers = ("C","D","A","A","B")
Guesses=[]
score = 0
question_num=0

for question in questions:
    print("---------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("\nEnter your answer (A,B,C,D) : ").upper()
    Guesses.append(guess)
    
    if guess == Answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{Answers[question_num]} is the correct answer")
    question_num+=1

print("-----------------------------------------------")
print("                     RESULT                    ")
print("-----------------------------------------------")

print("Answers : ",end = "")
for answer in Answers:
    print(answer,end=" ")
print()

print("Guesses : ",end = "")
for guess in Guesses:
    print(guess,end=" ")
print()

score = (score/len(questions) * 100)
print(f"Your Score : {score}%")

