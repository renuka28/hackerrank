def swap_case_builtin(s):
    """ swap case using builtin method
    https://www.hackerrank.com/challenges/swap-case/problem
    Args:
        s(str) : string to swap case
    Returns
        s(str) : case swapped string
    """
    return s.swapcase()


def swap_case_list_comp(s):
    """ swap case using list comprehension method
    https://www.hackerrank.com/challenges/swap-case/problem
    Args:
        s(str) : string to swap case
    Returns
        s(str) : case swapped string
    """
    return "".join([letter.upper() if letter.islower() else letter.lower() for letter in s])


if __name__ == '__main__':
    s = "Www.HackerRank.com"
    print("builtin result {}".format(swap_case_builtin(s)))
    print("swap_case_list_comp result {}".format(swap_case_list_comp(s)))
    s = input("Enter string to swap - ")
    print("builtin result {}".format(swap_case_builtin(s)))
    print("swap_case_list_comp result {}".format(swap_case_list_comp(s)))
