from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        nextList = self.powerfulNextList(needle)
        print(nextList)
        tar, pos = 0, 0
        while tar < len(haystack):
            if haystack[tar] == needle[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = nextList[pos - 1]
            else:
                tar += 1

            if pos == len(needle):
                return tar - pos
        return -1

    def nextList(self, needle: str) -> List[int]:
        def nextYeld(i):
            for j in range(i, 0, -1):
                if needle[0:j] == needle[i - j + 1:i + 1]:
                    return j
            return 0

        re = [nextYeld(i) for i in range(len(needle))]
        return re

    def powerfulNextList(self, needle: str) -> List[int]:
        re = []
        re.append(0)
        x, now = 1, 0
        while x < len(needle):
            if needle[x] == needle[now]:
                now += 1
                x += 1
                re.append(now)
            elif now:
                now = re[now - 1]
            else:
                re.append(0)
                x += 1
        return re


if __name__ == '__main__':
    print(Solution().strStr('ababaabaabac', 'abaabac'))
