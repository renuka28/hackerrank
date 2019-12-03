import utils


def test_find_runner_up(nums=None, ans=None, interactive=None):
    import find_runner_up_score as rup
    if interactive:
        n = utils.readn("integer")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

    if nums == None:
        nums = [2, 3, 6, 6, 5]
        ans = 5

    utils.print_test_info("find_runner_up_builtin_1", nums, "nums")
    ret = rup.find_runner_up_builtin_1(nums)
    print("runner up = {}".format(ret), end=" ")
    utils.check_answer(ret, ans)
    print()

    utils.print_test_info("find_runner_up_builtin_2", nums, "nums")
    ret = rup.find_runner_up_builtin_2(nums)
    print("runner up = {}".format(ret), end=" ")
    utils.check_answer(ret, ans)
    print()

    utils.print_test_info("find_runner_up", nums, "nums")
    ret = rup.find_runner_up(nums)
    utils.check_answer(ret, ans)
    print()


def test_second_lowest_grade(grade_names=None, ans=None, interactive=None):
    import nested_lists as nl
    if interactive:
        grade_names = []
        n = utils.readn("students")
        for i in range(n):
            name = input(
                "enter {} name - ".format(i+1)).strip()
            grade = float(input(
                "enter {} grade - ".format(i+1)).strip())
            grade_names.append([name, grade])

    if grade_names == None:
        grade_names = [['Harry', 37.21], ['Berry', 37.21], [
            'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
        ans = ['Berry', 'Harry']

    utils.print_test_info("second_lowest_grade",
                          grade_names, "grade and names")
    ret = nl.second_lowest_grade(grade_names)
    print("Second lowest grade = {}".format(ret))
    utils.check_answer(ret, ans)
    print()


def test_finding_the_percentage(grade_names=None, ans=None, interactive=None):
    import finding_the_percentage as fp
    if interactive:
        n = utils.readn("students")
        grade_names = {}
        for i in range(n):
            name, * \
                line = input("enter {} name and marks - ".format(i+1)).split()
            scores = list(map(float, line))
            grade_names[name] = scores
        query_name = input(
            "enter name of the student for calculating percentage ")

    if grade_names == None:
        grade_names = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0,
                                                                                              60.0]}
        query_name = "Malika"
        ans = 56.0

    utils.print_test_info("finding_the_percentage",
                          grade_names, "name and grades")
    ret = fp.finding_the_percentage(grade_names, query_name)
    print("percentage = {}".format(ret))
    utils.check_answer(ret, ans)
    print()


def test_validate_and_parse_email(emails=None, ans=None, interactive=None):
    import validating_and_parsing_email as em
    if interactive:
        n = utils.readn("emails")
        emails = utils.read_n_strings(n, "name and email")

    if emails == None:
        emails = ["DEXTER <dexter@hotmail.com>",
                  "VIRUS < virus!@variable.:p >"]
        ans = ["DEXTER <dexter@hotmail.com>"]

    utils.print_test_info("test_validate_and_parse_email",
                          emails, "name and emails")
    ret = em.validate_and_parse_email(emails)
    print("valid emails = {}".format(ret))
    utils.check_answers(ret, ans)
    print()


def test_list_ops(ls=None, commands=None, ans=None, interactive=None):
    import lists as l
    if interactive:
        n = utils.readn("commands")
        commands = utils.read_n_strings(n, " of command")
        ls = []

    if ls == None:
        ls = []
        commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6",
                    "append 9", "append 1",  "sort", "print", "pop", "reverse", "print"]
        ans = [9, 5, 1]

    utils.print_test_info("test_list_ops_1", commands, "commands")
    l.test_list_versions(ls.copy(), commands, ans, l.list_ops_1)

    utils.print_test_info("test_list_ops_2", commands, "commands")
    l.test_list_versions(ls.copy(), commands, ans, l.list_ops_2)

    utils.print_test_info("test_list_ops_3", commands, "commands")
    l.test_list_versions(ls.copy(), commands, ans, l.list_ops_3)


def test_tuples(integer_list=None, ans=None, interactive=None):
    import tuples as t
    if interactive:
        n = int(input("total number of integers - "))
        integer_list = map(int, input(
            "enter {} integers seprated by space = ".format(n)).split())

    if integer_list == None:
        integer_list = [1, 2, 3, 4]
        ans = 89902565

    utils.print_test_info("test_tuples", integer_list, "integer list")
    ret = t.get_hash(integer_list)
    print("hash = {}".format(ret))
    utils.check_answer(ret, ans)
    print()


def test_validating_uid_regex(uids=None, ans=None, interactive=None):
    import validating_uid_regex
    if interactive:
        n = utils.readn("uids")
        uids = utils.read_n_strings(n, " uid")
        ans = [None] * len(uids)
    if uids == None:
        import utils
        import os
        dir_name = os.path.dirname(os.path.abspath(__file__))
        uids = utils.listify(os.path.join(dir_name, "data\\ids.txt"))
        ans = utils.listify(os.path.join(dir_name, "data\\ids_ans.txt"))

    utils.print_test_info("test_validating_uid_regex", uids, "uids")
    ret_vals = []
    for i in range(len(uids)):
        ret_val = validating_uid_regex.is_valid_uid(uids[i])
        ret_vals.append('Valid' if ret_val else "Invalid")
    utils.check_answers(ret_vals, ans)
    print()


def test_swapcase(strings=None, ans=None, interactive=None):
    import swapcase
    if interactive:
        n = utils.readn(" - string count")
        strings = utils.read_n_strings(n, " string")

    if strings == None:
        strings = ["TEMP", "Temp", "tEMP", "TemP"]
        ans = ["temp", "tEMP", "Temp", "tEMp"]

    utils.print_test_info("swapcase", strings, "strings")
    ret = [swapcase.swap_case_list_comp(s) for s in strings]
    utils.check_answers(ret, ans)
    print()


def test_split_join_string(strings=None, ans=None, interactive=None):
    import string_split_join
    if interactive:
        n = utils.readn(" - string count")
        strings = utils.read_n_strings(n, " string")

    if strings == None:
        strings = ["this is a string", "this is not a string"]
        ans = ["this-is-a-string", "this-is-not-a-string"]

    utils.print_test_info("split_and_join_easy", strings, "strings")
    ret_vals = [string_split_join.split_and_join_easy(s) for s in strings]
    utils.check_answers(ret_vals, ans)
    print()

    utils.print_test_info("split_and_join", strings, "strings")
    ret_vals = [string_split_join.split_and_join(s) for s in strings]
    utils.check_answers(ret_vals, ans)
    print()


def test_string_whats_your_name(strings=None, ans=None, interactive=None):
    import string_whats_your_name
    if interactive:
        strings = utils.read_n_strings(
            2, "enter first and last name in separate lines \n ")

    if strings == None:
        strings = ["Ross", "Taylor"]
        ans = "Hello Ross Taylor! You just delved into python."

    utils.print_test_info("string_whats_your_name",
                          strings, "first and last names")
    ret_vals = string_whats_your_name.print_full_name(strings[0], strings[1])
    utils.check_answer(ret_vals, ans)
    print()


if __name__ == '__main__':
    test_find_runner_up()
    # test_find_runner_up(interactive=True)
    test_second_lowest_grade()

    gn = [['Harsh', 20.0], ['Beria', 20.0], [
        'Varun', 19.0], ['Kakunami', 19.0], ['Vikas', 21.0]]
    a = ['Beria', 'Harsh']
    test_second_lowest_grade(grade_names=gn, ans=a)

    test_finding_the_percentage()
    # test_validate_and_parse_email(interactive=True)

    emails_in = ['dheeraj <dheeraj-234@gmail.com>', 'crap <itsallcrap>', 'harsh <harsh_1234@rediff.in>', 'kumal <kunal_shin@iop.az>',
                 'mattp <matt23@@india.in>', 'harsh <.harsh_1234@rediff.in>', 'harsh <-harsh_1234@rediff.in>']
    ans = ['dheeraj <dheeraj-234@gmail.com>',
           'harsh <harsh_1234@rediff.in>', 'kumal <kunal_shin@iop.az>']
    test_validate_and_parse_email(emails=emails_in, ans=ans)

    test_list_ops()
    test_tuples()
    test_validating_uid_regex()
    test_swapcase()
    test_split_join_string()
    test_string_whats_your_name()
