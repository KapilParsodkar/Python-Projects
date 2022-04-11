print("welcome to the tip calculator")
total_bill=input("what was total bill?")
tip=input("what percentage tip would you like to give?10,12,15")
bill=int(total_bill)
total_tip=int(tip)
tip_percentage=(bill*total_tip)/100
print(tip_percentage)
people_divide_bill=input("How many people will divide bill?")
bill_divide=int(people_divide_bill)
each_person_should_pay_how_much= (tip_percentage+bill)/bill_divide
each_person_bill=round(each_person_should_pay_how_much,2)

print(f"each person should pay ${each_person_bill}")