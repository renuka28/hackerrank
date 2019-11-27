# # ------------------------------------------------------------------------------

# Objective
# In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!
# we have tried to do the calculations without using standard built in functions

# Task
# Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

# Note: Other than the modal value(which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place(i.e., ,  format).

# Input Format

# The first line contains an integer, , denoting the number of elements in the array.
# The second line contains  space-separated integers describing the array's elements


def mean(nums):
    """
    computes mean for the given list integers

    Args:
        nums (list of ints): list of numbers whose mean will be computed
    returns: 
        int: mean of nums
    """
    s = 0
    count = 0
    for num in nums:
        s += num
        count += 1
    return s/count


def median(nums):
    """
    computes median for the given list integers. If the list contains even number of digits
    then the function will compute the average of center two integers

    Args:
        nums (list of ints): list of numbers whose median will be computed
    returns: 
        int: median of nums
    """
    nums_sorted = sorted(nums)
    median = 0
    middle_num = int(len(nums_sorted)/2)
    if (len(nums_sorted) % 2) == 0:
        median = (nums_sorted[middle_num] + nums_sorted[middle_num - 1])/2
    else:
        median = nums_sorted[middle_num]
    return median


def mode(nums):
    """
    computes mode for the given list integers. If the list contains more than one mode then 
    the function returs the smallest mode

    Args:
        nums (list of ints): list of numbers whose mode will be computed
    returns: 
        int: mode of nums
    """
    frequency = {}
    nums_sorted = sorted(nums)
    for num in nums_sorted:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    modes = []
    max = -1
    for key in frequency:
        if(frequency[key] > max):
            modes.clear()
            modes.append(key)
            max = frequency[key]
        elif(frequency[key] == max):
            modes.append(key)
    return min(modes)


n = input("count (n) of integers - ")
nums_str = input(
    "enter {} ints separated by space in a single line - ".format(n)).split()
nums = list(map(int, nums_str))

print("mean = {}".format(mean(nums)))
print("median = {}".format(median(nums)))
print("mode = {}".format(mode(nums)))
