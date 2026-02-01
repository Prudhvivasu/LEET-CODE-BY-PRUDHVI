# LeetCode 7: Reverse Integer
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def reverse(self, x):
        t = str(x)
        r = t[::-1]
        if x >= 0:
            y = int(r)
        else:
            s = r[:-1]
            y = -int(s)
        if -(2**31 - 1) <= y <= (2**31):
            return y
        else:
            return 0
