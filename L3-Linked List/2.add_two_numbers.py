"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rollover = 0
        fake_head = ListNode(0)
        tail = fake_head
        node1 = l1
        node2 = l2

        while node1 or node2 or rollover>0:
            x = 0
            if node1:
                x += node1.val
            if node2:
                x += node2.val
            x += rollover
            rollover = x // 10
            x = x % 10

            node = ListNode(x)
            tail.next = node
            tail = node

            if node1: node1 = node1.next
            if node2: node2 = node2.next
        
        return fake_head.next

        