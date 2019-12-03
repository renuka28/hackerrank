def split_and_join_easy(line):
    return line.replace(" ", "-")
    # write your code here


def split_and_join(line):
    return "-".join(line.split())
    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join_easy(line)
    print(result)
    result = split_and_join(line)
    print(result)
