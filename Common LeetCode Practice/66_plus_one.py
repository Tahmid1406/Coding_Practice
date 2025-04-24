"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # start traversing the list backwards
        for i in range(len(digits)-1, -1, -1):

          #if number is 9, replace it with 0
          if digits[i] == 9:
            digits[i] = 0
          # if not 9, add 1 and return the list from here
          else:
            digits[i] += 1
            return digits

        # this return will only occur if the array is fully finished, meaning all are 9's
        # in that case we add a one at the front
        # for example, [9,9] --> [1,0,0]
        return [1] + digits