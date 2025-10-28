# email validation checker
# email=input("Enter your email : ")  #g@g.in
# if len(email)>=6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@")==1):
#             print("Entered email is right ")
#             pass
#         else:
#             print("Wrong email entered")
#         pass
#     else:
#         print("Wrong email entered ")
#     pass
# else:
#     print("Wrong email 1 ")

# ----------------------------------------------------------


# shopping cart project
# foods = []
# prices = [100,200,300,400,500]
# total = 0

# while True:
#     print("Enter food names to buy from online store [max=5]")
#     food = input("What kind of food do you want to buy? (enter 'q' to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         try:
#             foods.append(food)
#         except ValueError:
#             print("Invalid price. Please enter a number.")

# print("__________Your Cart__________")
# if not foods:
#     print("Your cart is empty.")
# else:
#     for i in range(len(foods)):
#         print(f"{foods[i]}: ${prices[i]:.2f}")
#     for price_item in prices:
#         total += price_item

#     print("-----------------------------")


# -----------------------------------------------------------------------------------------