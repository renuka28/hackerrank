# Day 1: Standard Deviation

# Objective
# In this challenge, we practice calculating standard deviation.
# Task
# Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem


from math import sqrt


def std_dev(nums):
    from mean_median_mode import mean
    sum = 0
    m = mean(nums)

    for num in nums:
        sum += (num - m) ** 2
    return (sqrt(sum/len(nums)))
