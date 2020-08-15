"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if 0 < sales < 1000:
        bonus = sales * 0.1  # apply 10% bonus when sales is less than $1000
        print("Your bonus is: ${:.2f}".format(bonus))
    else:
        bonus = sales * 0.15  # apply 15% bonus when sales is greater or equal to $1000
        print("Your bonus is: ${:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))
print("Invalid sales")
