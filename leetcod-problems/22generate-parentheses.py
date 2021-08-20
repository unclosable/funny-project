from typing import List
import collections


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        re = collections.deque([])
        self.dfs(re, "", 0, 0, n)
        return list(re)

    def dfs(self, deque, str, l, r, n):
        if l > n or r > n or r > l: return
        if l == n and r == n:
            deque.append(str)
            return
        self.dfs(deque, str + '(', l + 1, r, n)
        self.dfs(deque, str + ')', l, r + 1, n)
        return


if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
