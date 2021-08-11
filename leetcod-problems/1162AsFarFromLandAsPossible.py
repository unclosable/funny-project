# https://leetcode-cn.com/problems/as-far-from-land-as-possible/
import collections
from typing import List

xMove = [-1, 0, 1, 0]
yMove = [0, -1, 0, 1]


class Solution:

    def maxDistance(self, grid: List[List[int]]) -> int:
        f = grid[0][0]
        maxFar = -1
        checked = False
        for _ in grid:
            for i in _:
                if f != i:
                    checked = True
                    break
        if checked:
            maxFar = self.bfs(grid)

        return maxFar

    def bfs(self, grid: List[List[int]]):
        que = collections.deque([])
        for x, _ in enumerate(grid):
            print(f'x-{x}')

            print(_)
            for y, v in enumerate(_):
                print(f'y-{y}')
                if v:
                    print(f'append ({x},{y})')
                    que.append((x, y))
        far = -1
        while len(que) != 0:
            far += 1
            print('------')
            for _ in range(len(que)):
                now = que.popleft()
                print(now)
                (x, y) = now
                for i in range(4):
                    if 0 <= x + xMove[i] < len(grid) \
                            and 0 <= y + yMove[i] < len(grid):
                        if not grid[x + xMove[i]][y + yMove[i]]:
                            que.append((x + xMove[i], y + yMove[i]))
                            grid[x + xMove[i]][y + yMove[i]] = 1
        return far


if __name__ == '__main__':
    mark = [[False for _ in range(4)] for row in range(4)]

    print(Solution().maxDistance([[1, 0, 1],
                                  [0, 0, 0],
                                  [1, 0, 1]]))
    # print(mark)
