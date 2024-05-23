import numpy as np


def findLis(nums):
    if type(nums) is not list:
        raise TypeError('nums must be list')
    for i in range(len(nums)):
        if type(nums[i]) is not int and type(nums[i]) is not float:
            raise ValueError('nums must contain numbers')

    if len(nums) < 2:
        return len(nums)

    dp = np.ones(len(nums))
    for i in range(len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return int(max(dp))



