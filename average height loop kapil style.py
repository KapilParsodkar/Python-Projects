student_heights=input(" whats the height of students").split()
sh=len(student_heights)
for i in range(0,sh):
    student_heights[i]=int(student_heights[i])
print(sum(student_heights))

total_height=0
for kapi in student_heights:
    total_height+=kapi
print(f" total height is equal to {total_height}")


numofstudents=0
for maxi in student_heights:
    numofstudents+=1
print(f" the number of students are equal to {numofstudents}") 


average=round(total_height/numofstudents) 
print(average)  

