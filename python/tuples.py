

def get_hash(integer_list: list):
    return hash(tuple(integer_list))


if __name__ == '__main__':
    n = int(input("total number of integers - in tuples.py"))
    integer_list = map(int, input(
        "enter {} integers seprated by space = ".format(n)).split())
    print("hash = {}".format(get_hash(integer_list)))
