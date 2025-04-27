"""
9. Palindrome Number.
Given an integer x, return true if x is a palindrome, and false otherwise.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = abs(x)
        while(num != 0):
            rev = rev * 10
            rem = num%10
            rev += rem
            num //=10

        if rev == abs(x):
          return True
        else:
          return False

sol= Solution()
sol.isPalindrome(-121)