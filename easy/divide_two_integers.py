"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""

class Solution(object):
    def util(self, dividend, divisor):
        if divisor == dividend:
            return 1
        if dividend == 0 or divisor > dividend:
            return 0

        y = divisor
        x = dividend
        shifts = 0 

        while (y << 1) <= x:
            shifts += 1
            y <<= 1

        new_dividend = x - y
        new_divisor = divisor
        res = 0
        divisor = y

        while x >= y:
            y+=divisor
            res += 1

        return (res<<shifts) + self.divide(new_dividend,new_divisor)    
    
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_neg = (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0)
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        result  = self.util(dividend,divisor)
        if is_neg:
            result = -result
            return max(result,-2**31)
        
        return min(result, (2**31) -1)        
        