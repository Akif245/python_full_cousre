from calc_logo import logo
print(logo)

'''operations=['+','-','*','/','%']
print(operations)
option=input("Enter your option from the given above \n")
num1=int(input ("Enter your number1\n"))
num2=int(input ("Enter your number2\n"))
if option=='+':
    result=num1+num2
    print(f"Your answer is {result}")
elif option=='-':
    result=num1-num2
    print(f"Your answer is {result}")
elif option=='*':
    result=num1*num2
    print(f"Your answer is {result}")
elif option=='/':
    result=num1/num2
    print(f"Your answer is {result}")
elif option=='%':
    result=num1%num2
    print(f"Your answer is {result}")
else:
    print("Incorrect operation intered\n")
'''

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1=int(input("Enter your number 1 \n"))
num2=int(input("Enter your number 2 \n"))
for items in operations:
    print(items)
user_smbl=input("Select an operation from above \n")
calc_fcn = operations[user_smbl]
first_answer = calc_fcn(num1, num2)

continue_opp=input("Enter 'y' to continue or 'n' to stop\n")
if continue_opp=='y':
    user_smbl = input("Pick an operation: ") 
    num3 = int(input("What's the next number?: "))

    calc_fcn = operations[user_smbl] 

    second_answer = calc_fcn(calc_fcn(num1, num2), num3)

    second_answer = calc_fcn(first_answer, num3)

    print(f"{first_answer} {user_smbl} {num3} = {second_answer}")

elif continue_opp=='n':
    print(f" Your answer is {first_answer}")

