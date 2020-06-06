"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = -1 * int(str(x*-1)[::-1])
        else:
            result = int(str(x)[::-1])
        
        if(abs(result) > (2 ** 31 - 1)):
            return 0
        
        return result