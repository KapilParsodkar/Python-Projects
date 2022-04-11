

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division (n1,n2):
    return n1/n2

op={"+":add,"-":sub,"*":multiply,"/":division}
def calculator():

    num1=float(input(" what would be your first number? : "))
    for symbols in op:
        print(symbols)
    should_continue=True
    
    while should_continue:
        choice_of_operations=input("what would be your choice of operation? : ")
        num2=float(input("what would be your second number of calculation? : "))
        operationf=op[choice_of_operations]
        ans=operationf(num1,num2)
        print(f"{num1} {choice_of_operations} {num2} = {ans}")
        
        ycn=input(f" press 1 to continue with {ans} ,press 2 to start new calculations or press anything to exit : ")
        if ycn=="1":
            num1=ans
        elif ycn =="2":
            should_continue=False
            calculator() # this method is called recursion
        else:
            should_continue=False
            print("you have exited the calc")
calculator() 