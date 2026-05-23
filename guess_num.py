import random

x=input("type a number: ")

"""print("Welcome to guess the number game")

play=input("Do you want to play? ")
if play.lower() !="yes":
    quit()
    
print("Okay! Let's play :")
guess=0
while guess != x:
    guess=int(input("guess a number between 1 and 10: "))
    if guess < x:
        print("too low!")
    elif guess > x:
        print("too high!")
    else:
        print("you guessed it right!")
"""


if x.isdigit():
    x=int(x)
    
    if x<=0:
        print("please enter a larger number than 0 next time!")
        quit()
        
else:
    print("please enter a number next time!")
    quit()
        
random_num=random.randint(0,x)
guesses=0
while True:
    guesses += 1
    user_guess=input("make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please enter a valid number!")
        continue
        
    if user_guess == x:
        print("you got it")
        break
    else:
        print("you got it wrong")
        
print(f"you got it in {guesses} guesses!")
       