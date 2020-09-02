"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
# print(CODE_TO_NAME)
# task 3
# Change input to all uppercase

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        message = "{} is {:<28}"
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# task 4
# Use for loop to print out all state abbreviations and names

for state in CODE_TO_NAME:
    message = "{:<3} is {:<3}"
    print(message.format(state, CODE_TO_NAME[state]))