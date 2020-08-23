import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
number_of_picks = int(input("How many picks? "))
# Ask user to enter a positive integer
while number_of_picks < 0:
    print("Please enter a positive integer")
    number_of_picks = int(input("How many picks? "))

# Write  nested "for" loops to append random numbers until condition is met
for i in range(number_of_picks):
    number_list = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in number_list:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        number_list.append(number)
        number_list.sort()
    print(" ".join("{:2}".format(number) for number in number_list))  # Print numbers using join method
