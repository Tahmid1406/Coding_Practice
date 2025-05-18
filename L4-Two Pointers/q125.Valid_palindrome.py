"""
Q.125 Valid Palindrome (Two Pointer)
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
      """
      Two steps to solve
      1. Cleanup
      2. use two pointers to check if palindrome or not
      """

      # clearup or prapare the string before checking
      s= s.lower()
      s = [c for c in s if c.isalnum()]
      n = len(s)

      # using two pointers for palindrome check
      left = 0
      right = n-1

      while left <= right:
        if s[left] != s[right]:
          return False
        left += 1
        right -= 1

      return True




