import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_actions=[rock, paper, scissors]
end=False
while not end:
        user_actions=int(input("please choose the action\n press 0 for rock, 1 for paper , 2 for scissors "))
        print("you choose " + game_actions[user_actions])
        
        computer_actions=random.randint(0,2)
        print("Computer chose:")
        print(game_actions[computer_actions])
        
        if user_actions>=3 or user_actions<0:
            print("you have chosen invalid values lost")
        elif user_actions==0 and computer_actions==1:
            print("you lost")
        elif user_actions==0 and computer_actions==2:
            print("you won")
        elif user_actions==0 and computer_actions==0:
            print("match has drawn")
        elif user_actions==1 and computer_actions==0:
            print("you won")
        elif user_actions==1 and computer_actions==1:
            print("match has drawn")
        elif user_actions==1 and computer_actions==2:
            print("you lose")
        elif user_actions==2 and computer_actions==0:
            print("you lose")
        elif user_actions==2 and computer_actions==1:
            print("you won")
        elif user_actions==2 and computer_actions==2:
            print("match has drawn")
        
        play_again=input(" do you want to play the game agaon? yes or no").lower()
        if play_again=="no":
            end=True
            print("you have exited the game")
        
    
