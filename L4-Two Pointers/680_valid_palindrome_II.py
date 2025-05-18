"""
680 valid palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba" Output: true

Example 2:
Input: s = "abca" Output: true Explanation: You could delete the character 'c'.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

      def checkPalindrome(s:str, start:int, end:int) -> bool:
        left = start
        right = end

        while left < right:
          if s[left] != s[right]:
            return False
          left += 1
          right -= 1
        return True


      n = len(s)
      # using two pointers for palindrome check
      left = 0
      right = n-1

      while left < right:
        if s[left] != s[right]:
            left_removal = checkPalindrome(s, left+1, right)
            right_removal = checkPalindrome(s, left, right-1)
            return left_removal or right_removal
        else:
            left += 1
            right -= 1
      return True