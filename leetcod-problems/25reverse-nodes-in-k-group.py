# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeMaker(nums: List[int]) -> ListNode:
    head = ListNode()
    currentNode = head
    prevNode = None
    for i in nums:
        currentNode.val = i
        currentNode.next = ListNode()
        prevNode = currentNode
        currentNode = currentNode.next
    prevNode.next = None
    return head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nextHead = head
        remainNum = 0
        while remainNum < k:
            if nextHead is None:
                return head
            remainNum += 1
            nextHead = nextHead.next

        subList = self.reverseKGroup(nextHead, k)
        newHead = self.reversTopNode(head, k)
        head.next = subList

        return newHead

    def reversTopNode(self, head: ListNode, k: int) -> ListNode:
        prevNode = None
        currentNode = head
        while k > 0:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            k -= 1
        return prevNode

    def reversBased(self, head: ListNode):
        _head = head
        reversedHead = None
        prevNode = None
        while _head:
            currentNode = _head
            _head = _head.next
            nextNode = currentNode.next
            if nextNode is None:
                reversedHead = currentNode
            currentNode.next = prevNode
            prevNode = currentNode
        return reversedHead


# TODO well this's too hard to me,the solution is copy from somewhere
if __name__ == '__main__':
    head = Solution().reverseKGroup(listNodeMaker([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 3)
    while head:
        print(head.val)
        head = head.next
