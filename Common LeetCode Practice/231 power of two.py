"""
231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      if n ==1:
        return True
      temp = 0
      while(n > 1):
        n = n/2
        print(n)
        temp = n

      if(temp==1):
        return True
      else:
        return False

sol = Solution()
sol.isPowerOfTwo(1)