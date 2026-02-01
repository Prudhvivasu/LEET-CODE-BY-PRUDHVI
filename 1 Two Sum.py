# LeetCode 1: Two Sum
# Difficulty: Easy
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(0, l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
