# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reNode = l1

        currentL1 = l1
        lastL1 = None
        currentL2 = l2
        flg = False
        while currentL1 is not None:
            if currentL2:
                add = currentL1.val + currentL2.val + (1 if flg else 0)
                currentL1.val = add % 10
                flg = add > 9
            else:
                break
            lastL1 = currentL1
            currentL1 = currentL1.next
            currentL2 = currentL2.next

        if flg and currentL2:
            lastL1.next = currentL2
            self.nodeAdd(currentL2, None, 1)
        elif flg and currentL1:
            self.nodeAdd(currentL1, None, 1)
        elif flg:
            self.nodeAdd(None, lastL1, 1)
        elif currentL2:
            lastL1.next = currentL2

        return reNode

    def nodeAdd(self, node: ListNode, laseNode: ListNode, add):
        if node:
            add = node.val + add
            node.val = add % 10
            if add > 9:
                self.nodeAdd(node.next, node, 1)
        else:
            laseNode.next = ListNode(1, None)


if __name__ == "__main__":
    l1 = ListNode(2, next=ListNode(4, ListNode(7, None)))
    l2 = ListNode(5, next=ListNode(6, ListNode(4, ListNode(9, None))))
    l = Solution().addTwoNumbers(l1, l2)
    print("---")
    while l:
        print(l.val)
        l = l.next
