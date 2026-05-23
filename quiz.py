"""print("Welcome to quiz game")

play=input("Do you want to play? ")

if play.lower() !="yes":
    quit()

print("Okay! Let's play :")
score=0
answer=input("what does DBMS stands for?")
if answer.lower() == "database management system":
    print("Correct!")
    score += 1
else: print("incorrect!")

answer=input("what does RAM stands for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: print("incorrect!")

answer=input("who is the MC of one piece?")
if answer.lower() == "luffy":
    print("Correct!")
    score += 1
else: print("incorrect!")

answer=input("what is the relationship between luffy and rayleigh?")
if answer.lower() == "uncle and nephew":
    print("Correct!")
    score += 1
else: print("incorrect!")

print(f"you got {score} questions correct!") 
print(f"you got {score/4*100}% questions correct!") """

print("Welcome to quiz game")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay! Let's play :")

score = 0

questions = {
    "what does DBMS stands for? ": "database management system",
    "what does RAM stands for? ": "random access memory",
    "who is the MC of one piece? ": "luffy",
    "what is the relationship between luffy and rayleigh? ": "uncle and nephew"
}

for question, correct_answer in questions.items():
    answer = input(question)

    if answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {score/len(questions)*100}% questions correct!")