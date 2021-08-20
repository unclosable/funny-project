class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


#
# delete kth node
# @param head ListNode类 the node
# @param k int整型 the k
# @return ListNode类
#
class Solution:
    def deleteKthNode(self, head, k):
        myHead = head
        flg = 1
        last = None
        while head.next:
            if flg == k:
                last.next = head.next
                break
            flg += 1
            last = head
            head = head.next

        return myHead
        # write code here


if __name__ == '__main__':
    h = Solution().deleteKthNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 3)
    print('-')
    while h:
        print(h.val)
        h = h.next
