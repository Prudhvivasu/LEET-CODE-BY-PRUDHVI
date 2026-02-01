# LeetCode 66: Plus One
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def plusOne(self, digits):
        r = 0
        for x in digits:
            r = r * 10 + x
        p = r + 1
        res = list(map(int, str(p)))
        return res
