# creating input based variable codes
unit=input("please enter unit of time\n")
unit=unit.upper()
quantity=int(input(f"Please enter how many {unit} you want to calculate\n"))
if unit=="HOUR":
    result=quantity*60*24
    print(result)
