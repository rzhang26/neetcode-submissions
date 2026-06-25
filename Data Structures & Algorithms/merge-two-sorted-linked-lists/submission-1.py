# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp
        self.l1 = list1
        self.l2 = list2

        while (self.l1 is not None) and (self.l2 is not None):
            if self.l1.val <= self.l2.val:
                tail.next = self.l1
                self.l1 = self.l1.next
            else:
                tail.next = self.l2
                self.l2 = self.l2.next

            tail = tail.next

        if self.l1 is not None:
            tail.next = self.l1
        elif self.l2 is not None:
            tail.next = self.l2

        return temp.next

