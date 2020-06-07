"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        pfx = ""
        for x, y in zip(strs[0], strs[-1]):
            print(x)
            print(y)
            if x == y: pfx+=x
            else: break
        return pfx