# contains code to drive various modules


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

    ret = mmm.mean(nums)
    print("mean = {}".format(ret), end=" ")
    if ans != None:
        print(" - {}".format("SUCCESS" if ret == ans[0] else "FAILURE"))
    ret = mmm.median(nums)
    print("median = {}".format(ret), end=" ")
    if ans != None:
        print(" - {}".format("SUCCESS" if ret == ans[1] else "FAILURE"))
    ret = mmm.mode(nums)
    print("mode = {}".format(ret), end=" ")
    if ans != None:
        print(" - {}".format("SUCCESS" if ret == ans[2] else "FAILURE"))
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

    if not interactive:
        print("testing with nums = {} ".format(nums))

    ret = qrtls.quartiles(nums)
    print("1st = {} 2nd = {} and 3rd = {}".format(
        ret[0], ret[1], ret[2]), end=" ")
    if ans != None:
        print(" - {}".format("SUCCESS" if ret == ans else "FAILURE"))
    print()


test_mean_median_mode()
test_weighted_mean()
test_quartiles()
test_quartiles(nums=[1, 2, 3, 4, 5, 6], ans=(2, 3.5, 5))
# test_quartiles(interactive=True)
