
# Electricity bill estimator
price_per_kwh_cents = float(input("Enter cents per kwh: "))
kwh_per_day = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = price_per_kwh_cents * kwh_per_day * billing_days/100
print("Estimated bill ${:.2f}".format(estimated_bill))

# Electricity bill estimator 2.0

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

choice = int(input("Which tariff? 11 or 31: "))
if choice == 11:
    price_per_kwh_dollars = TARIFF_11
else:
    price_per_kwh_dollars = TARIFF_31
kwh_per_day = float(input("Enter daily use in kwh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = price_per_kwh_dollars * kwh_per_day * billing_days
print("Estimated bill ${:.2f}".format(estimated_bill))
