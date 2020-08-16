"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    # score = float(input("Enter score: "))
    # print("Your score status is: {}".format(score_status(score)))
    score = random.randint(0, 100)
    print("Score {} is: {}".format(score, score_status(score)))


def score_status(score):
    # Use if statement to determine score status
    if score < 0:
        return "Invalid"
    elif 0 < score < 50:
        return "Bad"
    elif 50 <= score < 90:
        return "Passable"
    elif 90 <= score <= 100:
        return "Excellent"
    else:
        return "Invalid score"  # if score is greater than 100 or less than 0 then print invalid score


main()
