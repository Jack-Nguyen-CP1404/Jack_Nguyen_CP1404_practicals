"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
# Use if statement to determine score status
if score < 0:
    print("Invalid score")
elif 0 < score < 50:
    print("Bad")
elif 50 <= score < 90:
    print("Passable")
elif 90 <= score <= 100:
    print("Excellent")
else:
    print("Invalid score")  # if score is greater than 100 or less than 0 then print invalid score
