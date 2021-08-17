import collections


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "{": "}",
            "(": ")",
            "[": "]",
            "}": False,
            "]": False,
            ")": False,
        }
        que = collections.deque([])
        for i in s:
            if dic[i]:
                que.append(i)
            elif len(que) > 0 and dic[que.pop()] == i:
                continue
            else:
                return False
        return len(que) == 0
