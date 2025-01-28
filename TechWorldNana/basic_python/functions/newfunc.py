#creating a fucntion for not reapeating a code block
unit_name="hours"
unit_measure=24
def conversion_unit(unit_format, message):
  print(f"{unit_format} days are {unit_measure*unit_format} {unit_name}")
  print(message)
conversion_unit(24, "thank you")