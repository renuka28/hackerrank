def print_full_name(first_name, last_name):
    print_str = "Hello {} {}! You just delved into python.".format(
        first_name, last_name)
    print(print_str)
    return print_str


if __name__ == '__main__':
    first_name = input("enter first name - ")
    last_name = input("enter last name - ")
    print_full_name(first_name, last_name)
