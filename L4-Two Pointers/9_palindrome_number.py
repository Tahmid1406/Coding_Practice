"""
9 Palindrome number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121 Output: true Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121 Output: false Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

First solution is by using number reversing

"""

# first solution, by reversing a number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = abs(x)
        if(x<0):
            return False
        while(num != 0):
            rev = rev * 10
            rem = num%10
            rev += rem
            num //=10

        if rev == abs(x):
          return True
        else:
          return False

# second solution is with two pointers treating like a string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        n = len(string)
        left = 0
        right = n-1

        while(left < right):
          if string[left] != string[right]:
            return False
          left += 1
          right -= 1

        return True