
# Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("----- YOUR CART -------")
for food in foods:
    print(food, end=" ")
print()

for price in prices:
    total += price
print(f"Your total is: ${total}")

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy?(q to quit): ")
#     if food.lower() == 'q':
#         break
#     else:
#         price = float(input("Enter the price of food: "))
#         foods.append(food)
#         prices.append(price)
# print("---------Your Cart---------")
# for food in foods:
#     print(food, end=' ')
# print()
# for price in prices:
#     total += price
# print(f"Total price is ${total}")
