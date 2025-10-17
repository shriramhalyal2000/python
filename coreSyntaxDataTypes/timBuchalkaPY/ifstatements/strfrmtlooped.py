name=input("please enter your name:\n")
age=int(input(f"{name}, Please enter your age:"))
if age > 18:
  print(f"You are old enough to vote {name}.")
elif age==18:
  print(f"you must be voting for the first time, plesae excersise your right causitiously")
else:
  print(f"you are not old enough to vote {name}, please come back after {18-age} year")