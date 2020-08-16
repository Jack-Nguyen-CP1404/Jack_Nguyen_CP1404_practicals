"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
import random

# Create a temperature input file

MINIMUM_NUMBERS = 15
MAXIMUM_NUMBERS = 20


# Write floating numbers into input file
def main():
    in_file = open("temp_input.txt", 'w')
    line = 0
    while line <= MINIMUM_NUMBERS:
        floating_number = random.uniform(-200, 200)
        line += 1
        print(floating_number, file=in_file)
    in_file.close()
    in_file = open("temp_input.txt", 'r')
    out_file = open("temps_output.txt", 'w')
    for lines in in_file:
        fahrenheit_temp = float(lines)
        print(fahrenheit_to_celsius(fahrenheit_temp), file=out_file)
    in_file.close()
    out_file.close()


# Convert from celsius to fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


# Convert from fahrenheit to celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
