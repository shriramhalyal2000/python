name=input("Please enert yor name:\n")
age=int(input("{0}, please enetr your age".format(name)))
if age>=18:
  print(f"you are old enough to vote {name}")
else:
  print("pleae come back after {0} year".format(18-age))