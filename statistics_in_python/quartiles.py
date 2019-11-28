# Quartile
# The quartiles of an ordered data set are the  points that split the data set into  equal groups. The  quartiles are defined as follows:


# : The first quartile is the middle number between the smallest number in a data set and its median.
# : The second quartile is the median ( percentile) of the data set.
# : The third quartile is the middle number between a data set's median and its largest number.
# Computing the First and Third Quartile
# We will use the first method described in the Wikipedia:

# We will split the data into two halves, lower half and upper half:

# If there are an odd number of data points in the original ordered data set, do not include the median (the central value in the ordered list) in either half.

# If there are an even number of data points in the original ordered data set, split this data set exactly in half.

# The value of the first quartile () is the median of the lower half and the value of the third quartile () is the median of the upper half.

# https://www.hackerrank.com/challenges/s10-quartiles/tutorial

import mean_median_mode as mmm


def quartiles(nums):
    """ 
    This function find the 1st, 2nd and 3rd quartile of a given series

    Args:
        nums (list of ints): List of ints for which quartiles need to be found

    Returns:
        tuple: containing 1st, 2nd and 3rd quartile in that order

    """

    nums = sorted(nums)
    second_quartile = mmm.median(nums)
    nums_length = len(nums)
    if nums_length == 0:
        return None
    elif nums_length == 1:
        # if only one element all quartiles are same
        return (nums[0], nums[0], nums[0])

    start = 0
    upto = int(nums_length/2)
    first_quartile = mmm.median(nums[start:upto])

    start = upto
    if nums_length % 2 != 0:
        start += 1
    upto = nums_length
    third_quartile = mmm.median(nums[start:upto])

    return (first_quartile, second_quartile, third_quartile)
