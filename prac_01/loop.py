"""CP1404 - Practical 01 - Loops"""

# Display all of the odd numbers between 1 and 20

print("Odd numbers between 1 and 20 are: ")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100
print("Numbers counting in 10s from 0 to 100 are: ")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# count down from 20 to 1
print("Numbers counting down from 20 to 1 are:")
for j in range(20, 0, -1):
    print(j, end=' ')
print()

# print n stars
print("Display number of stars in one line")
number_of_stars = int(input("Enter number of stars: "))
for k in range(number_of_stars):
    print("*", end=' ')
print()

# print n lines of increasing stars

print("Display n lines of increasing stars")
number_of_stars = int(input("Enter number of stars: "))
for n in range(1, number_of_stars + 1):
    print(n * "*")
print()
