# contains code to drive various modules
def check_answer(ret, ans):
    return "" if ans == None else (" - " + "SUCCESS" if ret == ans else "FAILURE")


def test_mean_median_mode(nums=None, ans=None, interactive=False):
    import mean_median_mode as mmm
    print("testing - mean, median and mode ---------")
    ans = None
    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

    if nums == None:
        nums = [1, 2, 3, 4, 5, 6]
        ans = (3.5, 3.5, 1)
        print("input = {} ".format(nums))

    m = mmm.mean(nums)
    med = mmm.median(nums)
    mod = mmm.mode(nums)
    m_ans = ""
    med_ans = ""
    mod_ans = ""

    if ans != None:
        m_ans = check_answer(m, ans[0])
        med_ans = check_answer(med, ans[1])
        mod_ans = check_answer(mod, ans[2])

    print("mean = " + str(m) + m_ans + "\n" +
          "median = " + str(med) + med_ans + "\n" +
          "mode = " + str(mod) + mod_ans)
    print()


def test_weighted_mean(nums=None, weights=None,  ans=None, interactive=False):
    import weighted_mean as wm
    print("testing - weighted mean ---------")
    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

        weights_str = input(
            "enter {} weights separated by space in a single line - ".format(n)).split()
        weights = list(map(int, weights_str))
    if nums == None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        weights = [1, 2, 3, 4, 5, 6, 7]
        ans = 5
    print("nums = {} ".format(nums))
    print("weights = {} ".format(weights))
    ret = wm.weighted_mean(nums, weights)
    print("weighted mean = {}".format(ret), end=" ")
    if ans != None:
        print(" - {}".format("SUCCESS" if ret == ans else "FAILURE"))
    print()


def test_quartiles(nums=None, ans=None, interactive=False):
    import quartiles as qrtls
    print("testing - quartiles ---------")

    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))
        # print(round(wm.weighted_mean(nums, weights), 1))

    if nums == None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        ans = (2, 4, 6)

    print("testing with nums = {} ".format(nums))

    ret = qrtls.quartiles(nums)
    print("1st = {} 2nd = {} and 3rd = {}".format(
        ret[0], ret[1], ret[2]), end=" ")
    print(check_answer(ret, ans))
    print()


def test_inter_quartile_range(nums=None, freq=None, ans=None, interactive=False):
    import quartiles as qrtls
    print("testing - inter quartile range ---------")
    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

        freq_str = input(
            "enter {} frequencies separated by space in a single line - ".format(n)).split()
        freq = list(map(int, freq_str))

    if nums == None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        freq = [2, 2, 2, 2, 2, 2, 2]
        ans = (2, 4, 6)

    print("nums = {} ".format(nums))
    print("freqency = {} ".format(freq))

    q, qr = qrtls.inter_quartile_range(nums, freq)
    print("1st = {} and 3rd = {}. Interquartile range = {}".format(
        q[0], q[2], qr),  end=" ")
    print(check_answer(qr, ans))
    print()


def test_std_dev(nums=None, ans=None, interactive=False):
    import std_dev as std
    print("testing - standard deviation ---------")

    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))
        # print(round(wm.weighted_mean(nums, weights), 1))

    if nums == None:
        nums = [10, 20, 30, 40, 50]
        ans = 14.1

    print("testing with nums = {} ".format(nums))

    ret = std.std_dev(nums)
    print("std dev =  {}".format(ret), end=" ")
    print(check_answer(round(ret, 1), ans))
    print()


test_mean_median_mode()

test_weighted_mean()

test_quartiles()
test_quartiles(nums=[1, 2, 3, 4, 5, 6], ans=(2, 3.5, 5))
test_inter_quartile_range(nums=[1, 2, 3], freq=[3, 3, 4], ans=2)
test_inter_quartile_range(nums=[6, 12, 8, 10, 20, 16], freq=[
                          5, 4, 3, 2, 1, 5], ans=9.0)
nums = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4,
        5, 6, 7, 8, 9, 10, 20, 10, 40, 30, 50, 20, 10, 40, 30, 50]
freqency = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5,
            6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
# test_quartiles(interactive=True)

test_inter_quartile_range(nums=nums, freq=freqency, ans=30)

# test_std_dev(interactive=True)
