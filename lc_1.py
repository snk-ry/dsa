""" LC 1 | Two Sum
    https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        pair = {}

        for idx, num in enumerate(nums):
            if target - num in pair:
                return [idx, pair[target - num]]
            pair[num] = idx
