# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.prev, self.curr = None, head

        while self.curr is not None:
            self.nxt = self.curr.next
            self.curr.next = self.prev

            self.prev = self.curr
            self.curr = self.nxt

        return self.prev

