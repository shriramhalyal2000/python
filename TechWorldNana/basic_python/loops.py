# loops
unit_measure="hours"
unit_quant=24

def unit_conversion(unit, message):
    return f"{unit} days are {unit*unit_quant} {unit_measure}\n {message}"

unit_input=int(input("Enter the unit num:\n"))
message_input=input("Enter the message tp be displayed:\n")

unit=unit_conversion(unit_input, message_input)
print(unit)