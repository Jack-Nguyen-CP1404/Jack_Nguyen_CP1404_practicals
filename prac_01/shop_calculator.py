"""CP1404 - Practical 01 - Loops"""
"""Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92  """

number_of_items = int(input("Total number of items: "))
total_price = 0  # declare variable total_price

while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Total number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Please enter item price: $"))
    print("Price of item: $" + str(price_of_item))
    total_price += price_of_item  # Sum all item prices

# Condition for total price when it's over $100 then give 10% discount
if total_price > 100:
    total_price = total_price * 0.9  # 10% is applied to total price
print("Total number of item: " + str(number_of_items))
print("Total price for " + str(number_of_items) + " items is ${:.2f}".format(total_price))

