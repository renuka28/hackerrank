def listify(filename: str, print: bool = False):
    file_lines_as_list = [line.strip() for line in open(filename)]
    if (print):
        print(file_lines_as_list)
    return file_lines_as_list


if __name__ == '__main__':
    filename = input(
        "This program will listify a given file. Enter file name - ")
    listify(filename)
