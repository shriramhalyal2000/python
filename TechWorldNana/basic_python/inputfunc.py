#input based function

unit_name="hours"
unit_measure=24
def conversion_unit(unit, message):
  print(f"{unit} days are {unit*unit_measure} {unit_measure}")
  print(message)
unit_input=int(input("please enter unit\n"))
message=input("Message\n")
conversion_unit(unit_input, message)