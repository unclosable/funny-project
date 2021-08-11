import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        nodes = collections.deque([root])
        maxSum = None
        maxRe = 0
        re = 0
        while len(nodes) > 0:
            re += 1
            levelSum = 0
            for _ in range(len(nodes)):
                node = nodes.popleft()
                levelSum += node.val
                nodes += self.nextNodes(node)
            if not maxSum or maxSum < levelSum:
                maxSum = levelSum
                maxRe = re
        return maxRe

    def nextNodes(self, node: TreeNode):
        if node:
            left, right = node.left, node.right
            if left and right:

                return [left, right]
            elif left:
                return [left]
            elif right:
                return [right]
            else:
                return []
