"""
Palindrome linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Input: head = [1,2,2,1] Output: true

"""

# two pointer 0(n) space complexity solution

from typing import Optional
# here is one solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        node = head

        while node:
            array.append(node.val)
            node = node.next

        string = str(array)
        string = string.lower()
        string = [c for c in string if c.isalnum()]
        n = len(string)
        left = 0
        right = n-1

        while(left < right):
          if string[left] != string[right]:
            print(string[left])
            print(string[right])
            print("here")
            return False
          left += 1
          right -= 1

        return True


# o(1) space complexity solution

from typing import Optional
# find mid point
"""
solution is to use slow and fast pointer. One goes one step and fast goes 2 steps.
By taking two steps, we kinda making sure slow is in the middle and fast is at the end.
"""

# reverse second half

# compare the first and second half node by node

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      def findMidPoint(head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next

        if fast.next: # odd number of nodes
          slow = slow.next

        return slow

      def reverse_linked_list(head: ListNode) -> ListNode:
        prev_node = head
        node = head.next

        while node:
          next_node = node.next
          node.next = prev_node
          prev_node = node
          node = next_node

        head.next = None
        return prev_node

      if head is None:
        return True

      mid_node = findMidPoint(head)
      reversed_second_head = reverse_linked_list(mid_node)

      n1 = head
      n2 = reversed_second_head

      while n2:
        if n1.val != n2.val:
          return False
        else:
          n1 = n1.next
          n2 = n2.next
      return True

