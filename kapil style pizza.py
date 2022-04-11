print("welcome to kapil pizza")
size=input("what size of pizza do you prefer? s,m or l")
bill=0
if size=="s":
    print("you have selected small pizza \n the price of small pizza is 8$")
    bill+=8
elif size=="m":
    print("you have selected medium pizza \n the price of medium pizza is 10$")
    bill+=10
elif size=="l":
    print("you have selected large pizza \n the price of large pizza is 12$")
    bill+=12
else:
    print("you have selected the value which is invalid!")
    
add_vegetable=input(" Do you want vegetables? y or n")
if add_vegetable=="y":
    bill+=5
    print(" we are adding vegetables in pizza that would be 5$ more")
elif add_vegetable=="n":
    bill+=0
    print(" we are not adding vegetables in pizza ")
else:
    print("you have selected value which is invalid")
    
add_extra_cheese=input("Do you want extra cheese? y or n")
if add_extra_cheese =="y":
    bill+=3
    print("we are adding extra cheese that would be 3$ more")
elif add_extra_cheese=="n":
    bill+=0
    print("we will not add cheese")
else:
    print("you have selected value which is invalid")
    
print(f" you total bill for pizza is ${bill}")
    
