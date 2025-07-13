<<<<<<< HEAD
menu = {
    "A": "$4.50",
    "B": "$5.69",
    "C": "$34.90",
    "D": "$1.89",
    "E": "$2.46"
}

cart = []
total = 0.0

print("------MENU--------")
for key, value in menu.items():
    print(f"{key:5} : {value}")
print("------------------")

while True:
    food = input("Select an item or 'q' to quit: ").upper()
    if food == 'Q':
        break
    elif food in menu:
        cart.append(food)
        price = float(menu[food].replace("$", ""))
        total += price
    else:
        print("Invalid item. Please choose from the menu.")

print("\nItems in your cart:")
for item in cart:
    print(f"{item} - {menu[item]}")

print(f"Total: ${total:.2f}")
=======
menu = {
    "A": "$4.50",
    "B": "$5.69",
    "C": "$34.90",
    "D": "$1.89",
    "E": "$2.46"
}

cart = []
total = 0.0

print("------MENU--------")
for key, value in menu.items():
    print(f"{key:5} : {value}")
print("------------------")

while True:
    food = input("Select an item or 'q' to quit: ").upper()
    if food == 'Q':
        break
    elif food in menu:
        cart.append(food)
        price = float(menu[food].replace("$", ""))
        total += price
    else:
        print("Invalid item. Please choose from the menu.")

print("\nItems in your cart:")
for item in cart:
    print(f"{item} - {menu[item]}")

print(f"Total: ${total:.2f}")
>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
