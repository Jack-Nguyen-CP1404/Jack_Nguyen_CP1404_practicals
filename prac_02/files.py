# Task 1
in_file = open("name.txt", 'w')
name = input("Enter your name: ")
print("Your name is {}".format(name.title()), file=in_file)

# Task 2:

file = open("numbers.txt", 'r')
first_number = file.readline()
second_number = file.readline()
print(int(first_number) + int(second_number))
file.close()
# # Task 3:
total = 0
file = open("numbers.txt", 'r')
for line in file:
    number_in_line = int(line)
    total += number_in_line
file.close()
print("Total of all numbers in file is: {}".format(total))
