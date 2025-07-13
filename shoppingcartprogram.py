foods = []
prices = []
total = 0

while True:
    food = input("What kind of food do you want to buy? (enter 'q' to quit): ")
    if food.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of your {food}: $"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid price. Please enter a number.")

print("__________Your Cart__________")
if not foods:
    print("Your cart is empty.")
else:
    for i in range(len(foods)):
        print(f"{foods[i]}: ${prices[i]:.2f}")
    for price_item in prices:
        total += price_item

    print("-----------------------------")
    print(f"Your total is : ${total:.2f}")