# new calculator code for python knolwedge

def addition(num1, num2):
    result = num1 + num2
    print(f" {result} is expected addition result")

def substraction(num1, num2):
    result=num1-num2
    print(f"{result} is expect substraction")

def multiplication(num1, num2):
    result=num1*num2
    print(f"{result} is expected multiplied number")

def division(num1, num2):
    result=num1/num2
    print(f"{result} is ecpected division number")

print("calculation performs based on two numericals and performs basic mathamatic operations")
num1=float(input("Enter the first number:\n"))
num2 =float(input("Enter the second number:\n"))

operators=input("choose operators from thees \nAddition, \nSubtraction, \nMultiplication, \nDivision")