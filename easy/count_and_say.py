"""
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n>=1 and n<=30):
            if n == 1:
                return "1"
            prev = self.countAndSay(n-1)
            res = ""
            
            count = 1
            for i in range(len(prev)):
                if i+1 == len(prev) or prev[i] != prev[i+1]:
                    res += str(count) + prev[i]
                    count = 1
                else:
                    count += 1
            
            return res
        else:
            return ""
                    
                
            