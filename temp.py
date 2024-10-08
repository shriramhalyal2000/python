# creating a temperature conversion program from kelvin to celius and vice versa

import math

temp = float(input("Please eneter the temperature for conversion:\t"))
unit = input("Please enter the unit you want it converted to (Klevin K or Celcius C):\t ")

if unit=="K":
  convert=temp+273.15
  convert=round(convert, 3)
  print(f"The converted values is {convert} K^0")
elif unit=="C":
  convert=temp-273.15
  convert=round(convert, 3)
  print(f"The converted values is {convert} C^0")
else:
  print("You have entered something else try again")