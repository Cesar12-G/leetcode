"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        openers = ["[","{","("] 
        closers = ["]","}",")"]
        
        stack = [] 
        for i in s: 
            if i in openers: 
                stack.append(i) 
            elif i in closers: 
                pos = closers.index(i) 
                if ((len(stack) > 0) and (openers[pos] == stack[len(stack)-1])): 
                    stack.pop() 
                else: 
                    return False
        if len(stack) == 0: 
            return True
        else: 
            return False        
            
        