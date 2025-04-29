#importing calculator module
# functional module for calculator program
# function for addition
def add(x, y):
    return x+y
# function for subtraction
def sub(x, y):
    return x-y
# function for multiplication
def mul(x, y):
    return x*y
# function for division
def div(x, y):
    return x/y

print("Welcome to calculator")
print("Available operations from these options:\n 1.Addition, \n2.Subtraction, \3.Multiplication, \4.Division")
while True:
    choice = input("Choose your pick: \n1., \t2., \t3., \t4. \n")
    if choice in "1, 2, 3, 4":
        try:
            n1=float(input("Please enter the first number :\n"))
            n2=float(input("Please enter the second number:\n"))
        except ValueError:
            print("Please enter valid choice!.")

        if choice =="1":
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == "2":
            print(f"{n1} - {n2} = {sub(n1, n2)}")
        elif choice == "3":
            print(f"{n1} * {n2} = {mul(n1, n2)}")
        elif choice == "4":
            print(f"{n1} / {n2} = {div(n1, n2)}")
        elif choice =="0":
            break

        nextCal=input("if you want to continue calculation with Yes or No:\n")
        if nextCal=="No":
            break
    else:
        print("Please enter valid choice")