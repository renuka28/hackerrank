
# weighted mean


def weighted_mean(nums, weights):
    """
    computes weighted mean for the given list integers and weights. 

    Args: 

        nums (list of ints): list of numbers
        weights (list of ints): list of weights

    Returns:
        int: weighted mean
    """
    weighted_sum = 0
    weights_sum = 0
    for i in range(n):
        weighted_sum += nums[i] * weights[i]
        weights_sum += weights[i]

    return weighted_sum/weights_sum


n = input("count (n) of integers - ")
nums_str = input(
    "enter {} ints separated by space in a single line - ".format(n)).split()
nums = list(map(int, nums_str))

weights_str = input(
    "enter {} weights separated by space in a single line - ".format(n)).split()
weights = list(map(int, weights_str))

print(round(weighted_mean(nums, weights), 1))
