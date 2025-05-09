"""
258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
      while(num > 9):
        temp = 0
        while(num > 0):
          temp += num %10
          num //= 10
        num = temp
      return num


sol = Solution()
print(sol.addDigits(999))