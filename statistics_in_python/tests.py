# contains code to drive various modules


def test_mean_mdeian_mode(interactive=False):
    import mean_median_mode as mmm
    print("testing - mean, median and mode ---------")
    if interactive:
        n = input("count (n) of integers - ")
        nums_str = input(
            "enter {} ints separated by space in a single line - ".format(n)).split()
        nums = list(map(int, nums_str))

        print("mean = {}".format(mmm.mean(nums)))
        print("median = {}".format(mmm.median(nums)))
        print("mode = {}".format(mmm.mode(nums)))
    else:
        nums = [1, 2, 3, 4, 5, 6]
        print("input = {} ".format(nums))
        ret = mmm.mean(nums)
        print("mean = {} - {}".format(ret, "SUCCESS" if ret == 3.5 else "FAILURE"))
        ret = mmm.median(nums)
        print("median = {} - {}".format(ret, "SUCCESS" if ret == 3.5 else "FAILURE"))
        ret = mmm.mode(nums)
        print("mode = {} - {}".format(ret, "SUCCESS" if ret == 1 else "FAILURE"))
    print()


def test_weighted_mean(interactive=False):
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
        print(round(wm.weighted_mean(nums, weights), 1))
    else:
        nums = [1, 2, 3, 4, 5, 6, 7]
        weights = [1, 2, 3, 4, 5, 6, 7]
        ans = 5
        print("nums = {} ".format(nums))
        print("weights = {} ".format(weights))
        ret = wm.weighted_mean(nums, weights)
        print("weighted mean = {} - {}".format(ret,
                                               "SUCCESS" if ret == ans else "FAILURE"))
    print()


def test_quartiles(interactive=False):
    import quartiles as qrtls
    print("testing - quartiles ---------")

    if interactive:
        # n = input("count (n) of integers - ")
        # nums_str = input(
        #     "enter {} ints separated by space in a single line - ".format(n)).split()
        # nums = list(map(int, nums_str))

        # weights_str = input(
        #     "enter {} weights separated by space in a single line - ".format(n)).split()
        # weights = list(map(int, weights_str))
        # print(round(wm.weighted_mean(nums, weights), 1))
        pass
    else:
        nums = [1, 2, 3, 4, 5, 6, 7]
        ans = 5
        print("nums = {} ".format(nums))
        ret = qrtls.quartiles(nums)
        print("1st = {} 2nd = {} and 3rd = {} - {}".format(ret[0], ret[1], ret[2],
                                                           "SUCCESS" if ret == ans else "FAILURE"))
    print()


# test_mean_mdeian_mode()
# test_weighted_mean()
test_quartiles()
