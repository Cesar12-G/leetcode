"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        
        num = 0;
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if dict[s[i+1]] > dict[s[i]]:
                    num += dict[s[i+1]] - dict[s[i]]
                    i += 1                     
                else:
                    num += dict[s[i]]
            else:
                num += dict[s[i]]
            i += 1
        
        return num