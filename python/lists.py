def list_ops_1(ls: list, command_str: str):
    """ peforms various list operations based on the command list. 
    supported operations are
    1. insert i e: Insert integer  at position .
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer .
    4. append e: Insert integer  at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.
    refer to https://www.hackerrank.com/challenges/python-lists/problem for 
    more information

    IMPLEMENTAION USING SWITCH PATTERN

    Args:
         ls (list): list  on which operations will be performed
         command_str (str): command to perform 
    Returns:
         list : list after performing opeeration in command argument
    """
    def insert_element(ls: list, args: list):
        if ls == None:
            ls = list()
        ls.insert(int(args[0]), int(args[1]))
        return ls

    def print_list(ls: list, args: list = None):
        print(ls)
        return ls

    def remove_element(ls: list, args: list):
        if ls != None:
            try:
                ls.remove(int(args[0]))
            except(ValueError):
                pass
        return ls

    def append_element(ls: list, args: list):
        if ls == None:
            ls = list()
        ls.append(int(args[0]))
        return ls

    def sort_list(ls: list, args: list):
        if ls != None:
            desc = False
            if len(args) > 0 and args[0] == "desc":
                desc = True
            ls = sorted(ls, reverse=desc)
        return ls

    def pop_element(ls: list, args: list):
        if ls != None:
            try:
                ls.pop()
            except(IndexError):
                pass
        return ls

    def reverse_list(ls: list, args: list):
        if ls != None:
            ls.reverse()
        return ls

    switcher = {
        "insert": insert_element,
        "print": print_list,
        "remove": remove_element,
        "append": append_element,
        "sort": sort_list,
        "pop": pop_element,
        "reverse": reverse_list
    }

    command, *args = command_str.split()
    if command in switcher:
        ls = switcher[command](ls, args)
    return ls


def list_ops_2(ls: list, command_str: str):
    """ peforms various list operations based on the command list. 
    supported operations are
    1. insert i e: Insert integer  at position .
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer .
    4. append e: Insert integer  at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.
    refer to https://www.hackerrank.com/challenges/python-lists/problem for 
    more information

    IMPLEMENTAION USING eval 

    Args:
         ls (list): list  on which operations will be performed
         command_str (str): command to perform 
    Returns:
         list : list after performing opeeration in command argument
    """
    # eval cal be used to execute arbitrary code!!!!
    # check if it is in our list of supported ops
    supported_ops = ["insert", "print", "remove",
                     "append", "sort", "pop", "reverse"]
    command, *args = command_str.split()
    to_exec = ""
    if command in supported_ops:
        if command == "print":
            print(ls)
        else:
            to_exec += command+"(" + ",".join(args) + ")"
            eval("ls."+to_exec)
    return ls


def list_ops_3(ls: list, command_str: str):
    """ peforms various list operations based on the command list. 
    supported operations are
    1. insert i e: Insert integer  at position .
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer .
    4. append e: Insert integer  at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.
    refer to https://www.hackerrank.com/challenges/python-lists/problem for 
    more information

    IMPLEMENTAION USING getattr 

    Args:
         ls (list): list  on which operations will be performed
         command_str (str): command to perform 
    Returns:
         list : list after performing opeeration in command argument
    """

    supported_ops = ["insert", "print", "remove",
                     "append", "sort", "pop", "reverse"]
    function, *args = command_str.split()
    list_ops = dir(list)
    if function == "print":
        print(ls)
    elif function in supported_ops and function in list_ops:
        if len(args) == 0:
            getattr(ls, function)()
        elif len(args) == 1:
            getattr(ls, function)(int(args[0]))
        elif len(args) == 2:
            getattr(ls, function)(int(args[0]), int(args[1]))
    return ls


def check_answer(ret, ans):
    return "" if ans == None else (" - " + "SUCCESS" if ret == ans else "FAILURE")


def test_list_versions(ls, commands, ans, func):
    ls = ls.copy()
    print("Initial list =  {} ".format(ls))
    for command in commands:
        # print("Command = {}".format(command), end=" ")
        ls = func(ls, command)
        # print("List = {}".format(ls))
    print("final list = {}".format(ls), end=" ")
    print(check_answer(ls, ans))
    print()


if __name__ == '__main__':
    ls = []
    commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6",
                "append 9", "append 1",  "sort", "print", "pop", "reverse", "print"]
    ans = [9, 5, 1]

    print("testing - test_list_ops_1 ---------")
    test_list_versions(ls.copy(), commands, ans, list_ops_1)

    print("testing - test_list_ops_2 ---------")
    test_list_versions(ls.copy(), commands, ans, list_ops_2)

    print("testing - test_list_ops_3 ---------")
    test_list_versions(ls.copy(), commands, ans, list_ops_3)
