from typing import Optional

# https://neetcode.io/problems/reverse-a-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # two pointers solution - iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev, curr = None, head
      while curr:
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp
      return prev