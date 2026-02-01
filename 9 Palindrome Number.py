# LeetCode 9: Palindrome Number
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        t = s[::-1]
        if s == t:
            return True
        else:
            return False
