from num_art import logo
from random import randint
print(logo)
EASY_LEVEL=10
HARD_LEVEL=5
def check_ans(guess,answer,turns):
    if guess> answer:
        print("Too high\n")
        return turns-1
    elif guess<answer :
        print("Too Low\n")
        return turns-1
    else:
        print(f"Your guess is Correct {answer} \n")
    
def difficulty():
    level=input("choose 'easy' or 'hard':\n")
    if level=="easy":
        global turns
        return EASY_LEVEL
    else:
        return HARD_LEVEL
            
def game():
    print("WELCOME TO NUMBER GUESSING GAME !")
    print("I AM THINKING OF A NUMBER BETWEEN  1 TO 100 !")

    answer=randint(1,100)
    turns=difficulty()
    guess=0
    while guess!=answer:
        guess=int(input("Guess a number :"))
        print(f"You Have {turns} attempts to guess the number\n")
        turns=check_ans(guess,answer,turns)
game()

