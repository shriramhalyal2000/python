print("Hello world this is my first step towards devops as a career")
# variables
# variable= a container for a value (string, integer,float, boolean)
# variable behaves the way as if it contains the value
# strings contains alphanumerics
first_name = "Shriram"
food = "pizza"
email = "sshalyal42@gmail.com"

# integer= contains whole numbers without decimal point
age = 25    # does not need quotes because it contains only numbers
quantity = 30
time = 1145  # military format

# printing all the defined variables and strings in an output

print(f"you are {first_name}")  # here f"" represents formatting you can print the placeholder values inside
print(f"your age is {age}")
print(f"the laptops you want are {quantity} dell")

# float any numerical value with decimals on them

price = 22.4
gpa = 3.2
distance = 5.5

print(f"the cost of a milk packet is {price}")
print(f"your average gpa is {gpa}")
print(f">> the distance covered in marathon is {distance}")

# boolean values  they only have true or false outcome
is_developer = True
is_cicd = False

# example

if is_developer:
    print("you are a developer")
else:
    print("you are not a developer")

if is_cicd:
    print("you have not configured pipeline")
else:
    print("you have configured pipeline")
