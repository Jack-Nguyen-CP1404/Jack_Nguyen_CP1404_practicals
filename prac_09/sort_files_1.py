import os


def main():
    """Sort different file extensions to a new their folder"""
    os.chdir('FilesToSort')
    for file_name in os.listdir('.'):
        # Process files and ignore directories
        if os.path.isdir(file_name):
            continue
        file_extension = file_name.split('.')[-1]
        # Create new directory file for each extension
        # Don't create a file directory if existed
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        os.rename(file_name, "{}/{}".format(file_extension, file_name))
        print("{}/{}".format(file_extension, file_name))


main()
