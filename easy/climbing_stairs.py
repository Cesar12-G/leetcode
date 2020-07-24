"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
d = {}
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            d[n] = n
            return d[n]
        else:
            if n in d:
                return d[n]
            else:
                d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return d[n]
                    
                
            