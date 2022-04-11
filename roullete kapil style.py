import random
names_string = input("Give me everybody's names, separated by a comma. ")
#for spltting properly spacing between the name
names = names_string.split(",")
#for taking the values from 0 to the names given(their characters)
names1=len(names)
random_selection=random.randint(0,names1-1)
#names1-1 because the python starts counting from 0
pay_bill=names[random_selection]
print(pay_bill + " is going to pay the bill")