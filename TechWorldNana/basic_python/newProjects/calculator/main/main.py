# new calculator code for python knolwedge

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2
# print("calculation performs based on two numericals and performs basic mathamatic operations")
# num1=float(input("Enter the first number:\n"))
# num2 =float(input("Enter the second number:\n"))
#
# operators=input("choose operators from thees \nAddition, \nSubtraction, \nMultiplication, \nDivision")
# while True:
#     option=input("Choose your operation: Add, \nSub, \nMul, \nDiv")
#     if option in ("Add", "Sub", "Mul", "Div"):
#         n1=float(input("Enter number 1"))
#         n2=float(input("Enter number 2"))
#
#         if option=="Add":
#             print(f"{n1} + {n2} =", addition(num1, num2) )
#         elif option=="Subtraction":
#             print(f"{n1} - {n2} =", substraction(num1, num2))
#         elif option=="Multiplication":
#             print(f"{n1} * {n2} =", multiplication(num1, num2))
#         elif option=="Divsion":
#             print(f"{n1} / {n2} =", division(num1, num2))
#     else:
#         print("Invalid input please try again")
#     break

print("welcome to calculator")
print("Operation available are:\n 1.Add, \n2.Sub, \n3.Mul, \n4.Div")
while True:
    #provide choise to select the calculation task
    option=input("Choose your like from : \n \t1., \t2., \t3., \t4.:\n")
    if option in "1, 2, 3, 4, 0":
        try:
            n1=float(input("Please enter num1:\n"))
            n2=float(input("please enter num2:\n"))
        except ValueError:
            print("please enter the number again carefully!.")

        if option=="1":
            print(f"{n1} + {n2} = {addition(n1, n2)}")
        elif option=="2":
            print(f"{n1}- {n2} =  {subtraction(n1, n2)}")
        elif option=="3":
            print(f"{n1} * {n2} =  {multiplication(n1, n2)}")
        elif option=="4":
            print(f"{n1} / {n2} =  {division(n1, n2)}")
        elif option=="0":
            break

        use=input("Do you want to continue with calculation try YES or NO:\n")
        if  use=="NO":
            break
    else:
        print("please enter valid choice")