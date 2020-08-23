"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students.
    Comment out unwanted printing lines"""

    input_file = open(FILENAME)
    data_list = []  # Create an empty data_list
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data_list.append(parts)  # add parts to data_list
        subject_details(parts)
    input_file.close()
    return data_list


def subject_details(parts):
    print("{} is taught by {:13} and has {:>3} student".format(parts[0], parts[1], parts[2]))


main()
