
def check_answer(ret, ans):
    return "" if ans == None else (" - " + "SUCCESS" if ret == ans else "FAILURE")


def test_find_runner_up(nums=None, ans=None, interactive=None):
    import find_runner_up_score as rup
    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

    if nums == None:
        nums = [2, 3, 6, 6, 5]
        ans = 5

    print("testing - find_runner_up_builtin_1 ---------")
    print("nums = {} ".format(nums))
    ret = rup.find_runner_up_builtin_1(nums)
    print("runner up = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()

    print("testing - find_runner_up_builtin_2 ---------")
    print("nums = {} ".format(nums))
    ret = rup.find_runner_up_builtin_2(nums)
    print("runner up = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()

    print("testing - find_runner_up ---------")
    print("nums = {} ".format(nums))
    ret = rup.find_runner_up(nums)
    print("runner up = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()


def test_second_lowest_grade(grade_names=None, ans=None, interactive=None):
    import nested_lists as nl
    if interactive:
        grade_names = []
        n = int(input("count (n) of students - "))
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

    print("testing - second_lowest_grade ---------")
    print("grade and names = {} ".format(grade_names))
    ret = nl.second_lowest_grade(grade_names)
    print("Second lowest grade = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()


def test_finding_the_percentage(grade_names=None, ans=None, interactive=None):
    import finding_the_percentage as fp
    if interactive:
        n = int(input("count (n) of students - "))
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

    print("testing - finding_the_percentage ---------")
    print("name and grades = {} ".format(grade_names))
    ret = fp.finding_the_percentage(grade_names, query_name)
    print("percentage = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()


def test_validate_and_parse_email(emails=None, ans=None, interactive=None):
    import validating_and_parsing_email as em
    if interactive:
        n = int(input("count (n) of emails - "))
        emails = []
        for i in range(n):
            emails.append(input(
                "enter {} name and email separated by space - ".format(i+1)))

    if emails == None:
        emails = ["DEXTER <dexter@hotmail.com>",
                  "VIRUS < virus!@variable.:p >"]
        ans = ["DEXTER <dexter@hotmail.com>"]

    print("testing - test_validate_and_parse_email ---------")
    print("name and emails = {} ".format(emails))
    ret = em.validate_and_parse_email(emails)
    print("valid emails = {}".format(ret), end=" ")
    print(check_answer(ret, ans))
    print()
    print("\n".join(ret))


if __name__ == '__main__':
    # test_find_runner_up()
    # test_find_runner_up(interactive=True)
    # test_second_lowest_grade()

    # gn = [['Harsh', 20.0], ['Beria', 20.0], [
    #     'Varun', 19.0], ['Kakunami', 19.0], ['Vikas', 21.0]]
    # a = ['Beria', 'Harsh']
    # test_second_lowest_grade(grade_names=gn, ans=a)

    # test_finding_the_percentage()
    # test_validate_and_parse_email(interactive=True)
    # emails_in = ['dheeraj <dheeraj-234@gmail.com>', 'crap <itsallcrap>', 'harsh <harsh_1234@rediff.in>', 'kumal <kunal_shin@iop.az>',
    #              'mattp <matt23@@india.in>', 'harsh <.harsh_1234@rediff.in>', 'harsh <-harsh_1234@rediff.in>']
    # ans = ['dheeraj <dheeraj-234@gmail.com>',
    #        'harsh <harsh_1234@rediff.in>', 'kumal <kunal_shin@iop.az>']

    # test_validate_and_parse_email(emails=emails_in, ans=ans)
