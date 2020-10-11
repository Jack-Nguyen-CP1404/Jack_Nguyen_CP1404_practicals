"""
CP1404/CP5632 Practical_09
Clean up files that have different namings to file name that contains "_" between each word and file extension is ".txt"
"""

import os


def main():
    """Fix inconsistent file names."""
    os.chdir('Lyrics/Christmas')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            get_fixed_filename(filename)
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    words = []
    current_position = 0
    for next_position, letter in enumerate(filename):
        if letter.isupper() and current_position < next_position:
            words.append(filename[current_position:next_position])
            current_position = next_position
    words.append(filename[current_position:])
    new_name = '_'.join(words).replace("__", "_").replace("(_", "(")
    return new_name


main()
