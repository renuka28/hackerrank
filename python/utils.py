def listify(filename: str, print: bool = False):
    file_lines_as_list = [line.strip() for line in open(filename)]
    if (print):
        print(file_lines_as_list)
    return file_lines_as_list


def readn(prompt: str = None):
    """ prompts and reads an integer from stdin
    returns:
        n (int): read integer
    """
    return int(input("count (n) {} - ".format("" if prompt == None else prompt)))


def read_n_strings(n: int, prompt: str = None, prompt_as_is: bool = False):
    lines = []
    for i in range(n):
        input_str = prompt if prompt_as_is else "enter {} {} - ".format(
            i+1, ("" if prompt == None else prompt))
        lines.append(input(input_str))
    return lines


def check_answer(ret_val, answer):
    output = "returned value '{}' {} answer '{}' - {}"
    print(output.format(ret_val, " == ", answer, "SUCCESS") if ret_val
          == answer else output.format(ret_val, " != ", answer, "FAILURE"))


def check_answers(ret_vals, answers):
    if(ret_vals != None and answers != None):
        for i in range(len(answers)):
            check_answer(ret_vals[i], answers[i])
    else:
        print("can't do answer check as returned value = {} and answers = {}".format(
            ret_vals, answers))


def print_test_info(func_name: str, input=None, input_prompt: str = ""):
    print_str = "testing '{}'".format(func_name)
    line_length = 100
    pads = int((line_length - len(print_str))/2) - 1
    print_str = '-' * pads + " " + print_str + " " + '-' * pads
    print(print_str)

    if input != None:
        input_str = "Input " if (
            input_prompt == None or input_prompt == "") else input_prompt
        print("{} = {} ".format(input_str, input))


if __name__ == '__main__':
    filename = input(
        "This program will listify a given file. Enter file name - ")
    listify(filename)
