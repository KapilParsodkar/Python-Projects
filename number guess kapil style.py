import random
easyturns=10
hardturns=5
def checker(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        return turns-1
        print("too low")
    elif guess==answer:
        print(f"you got the answer the correct answer was {answer}")
        
def difficulty():
    level=input("choose the level in which you like to play the game easy or hard  ")
    if level=="hard":
        return hardturns
    elif level=="easy":
        return easyturns
    
def game():
    print("welcome to the game of guessing the number  ")
    print("computer is thinking of a number  ")
    answer=random.randint(1,100)
    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} remaining")
        
        guess=int(input("guess the number"))
        
        turns=checker(guess, answer, turns)
        if turns==0:
            print(f"you are out of guesses you lose the correct answer is  {answer}")
            return
        elif guess != answer:
            print("guess again")
game()