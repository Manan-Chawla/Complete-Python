# asking user to enter weight
weight=float(input("enter your weight --> "))
# asking user to choose unit in k or pounds
unit=input("Kilogram or pound ? k or p : ")

if unit=="k":
    weight=weight*2.205
    unit="Lbs."
    print(f"Weight is {weight} in {unit}")
elif unit=="p":
    weight=weight/2.205
    unit="Kgs."
    print(f"Weight is {weight} in {unit}")
else:
    print("wrong unit entered")
