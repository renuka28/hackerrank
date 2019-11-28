
# weighted mean


def weighted_mean(nums, weights, n=0):
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
    if(n == 0):
        n = len(nums)

    for i in range(n):
        weighted_sum += nums[i] * weights[i]
        weights_sum += weights[i]

    return weighted_sum/weights_sum
