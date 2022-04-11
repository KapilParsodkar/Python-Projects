print('welome to treasure island \n your mission is to find the treasure')
leftorright=input("where you wanna go left or right?\n l or r ").lower()
if leftorright =="l":
    swimorwait=input("you are in the game so do you wanna swim or wait?\n s or w" ).lower()
    if swimorwait=="w":
        whichdoor=input(" you are still in game which door you wanna go through red,blue,yellow\n r,yor b").lower()
        if whichdoor=="y":
            print("you won the game")
        elif whichdoor=="r":
            print("you are burned by fire")
        elif whichdoor=="b":
            print("you are eaten by beast game over")
        else:
            print("the game is over")
        
           
    else:
        print("you are attacked by the trout the game is over")
else:
    print(" you fall into a hole game over")