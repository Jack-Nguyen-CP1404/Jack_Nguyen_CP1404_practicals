import os


def main():
    """Sort different file extensions to a new their folder by user input"""
    os.chdir('FilesToSort')
    extension_dict = {}
    for file_name in os.listdir('.'):
        # Process files and ignore directories
        if os.path.isdir(file_name):
            continue
        file_extension = file_name.split('.')[-1]
        file_type = input("What category would you like to sort {} files into? ".format(file_extension))
        # Map user input to file_extension in extension_dict and move to its folder name
        extension_dict[file_extension] = file_type
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        os.rename(file_name, "{}/{}".format(extension_dict[file_extension], file_name))
        print("{}/{}".format(extension_dict[file_extension], file_name))


main()
