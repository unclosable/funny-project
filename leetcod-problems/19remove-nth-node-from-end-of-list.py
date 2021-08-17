# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        f, s = head, head
        for i in range(n):
            if f.next:
                f = f.next
            else:
                return head.next
        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return head
