"""
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Coud you solve it without converting the integer to a string?
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            num = x
            r = 0
            while num > 0:
                mod = num % 10
                num = (num - mod) / 10
                r = r * 10 + mod

            if x == r:
                return True
            else:
                return False
        else:
            return False