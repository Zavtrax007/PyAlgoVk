import numpy as np


def findLis(nums):
    if len(nums) < 2:
        return len(nums)

    dp = np.ones(len(nums))
    for i in range(len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


a = [3, 1, 4, 7, 2, 11, 9]
print(findLis(a))
