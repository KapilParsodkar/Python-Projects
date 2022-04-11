# 🚨 Don't change the code below 👇
line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

row=int(position[0])
col=int(position[1])
map[row-1][col-1]="x"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")