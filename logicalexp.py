# logical expressions in python evaluate multiple conditions and or not
# or - at least one condition must be True
# and =both conditions must be Truenot= inverts the condition(not flse, not true)

temp = 30
# is_raining=False
# # only one of these conditions i logically true is_raining is false!! dnot bother
# if temp >25 or temp <0 or is_raining:
#   print("Grab an umbrella")
# else:
#   print("No need to grab an umbrella")

is_sunny= True
if temp >=28 and is_sunny:
  print(f"Its too hot 🥵")
else:
  print("Its not too hot")