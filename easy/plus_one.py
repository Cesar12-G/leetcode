"""
66. Plus One
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        charList = [str(i) for i in digits]
        s = ''.join(charList)
        n = int(s) + 1
        int1 = str(n)   
        return [int(d) for d in str(int1)]