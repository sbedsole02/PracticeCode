#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        spoon = str(x)
        end = len(spoon)-1
        for index in range(len(spoon)):
            if spoon[index] != spoon[end]:            
                return False
            end = end-1
        return True
