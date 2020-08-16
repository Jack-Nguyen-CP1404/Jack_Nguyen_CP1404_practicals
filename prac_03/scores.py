"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    i = 0
    output_file = open("results.txt", 'w')
    numbers_of_score = int(input("Enter number of scores: "))

    # Use while loop to write results in output file
    while i <= numbers_of_score:
        score = random.randint(0, 100)
        i += 1
        print("{} is {}".format(score, score_status(score)), file=output_file)
    output_file.close()


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
