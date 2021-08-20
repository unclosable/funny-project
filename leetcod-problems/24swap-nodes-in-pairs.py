# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head in None or head.next is None:
            return head
        _head = head.next
        head.next = self.swapPairs(_head.next)
        _head.next = head
        return _head
