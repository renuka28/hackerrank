
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


if __name__ == '__main__':
    test_find_runner_up()
    test_find_runner_up(interactive=True)
