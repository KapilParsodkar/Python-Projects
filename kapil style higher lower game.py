from game_data import data
import random
from art import logo,vs


def get_random_data():
  return random.choice(data)

def format_d(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, is a {description}, from {country}"

def checker(guess,a_followers,b_followers):
    if a_followers > b_followers:
      return guess == "a"
    else:
      return guess == "b"


print(logo)
score=0
continue_game=True
a_account=get_random_data()
b_account=get_random_data()
while continue_game:
        a_account=b_account
        b_account=get_random_data()
        if a_account==b_account:
           b_account=get_random_data()
        print(f"Compare A: {format_d(a_account)}.")
        print(vs)
        print(f"Against B: {format_d(b_account)}.")
        guess=input(" choose a or b : ").lower()
        a_followers_count=a_account["follower_count"]
        b_followers_count=b_account["follower_count"]
        is_correct=checker(guess, a_followers_count, b_followers_count)
        print(logo)
        if is_correct:
         score+=1
       
         print(f"the answer is correct your current score is {score}")
        else:
         continue_game=False
         print(f"the answer is wrong you lose your current  is {score}")

            
            
    