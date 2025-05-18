"""
reversing a linked list

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional
class Solution(object):
  def linkedListRev(self, head: Optional[ListNode]) -> ListNode:
    prev_node = head
    node = head.next

    while(node):
      next_node = node.next
      node.next = prev_node
      prev_node = node
      node = next_node
    head.next = None
    return prev_node