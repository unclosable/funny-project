from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        can = self.charsNo(chars)
        re = 0
        print(can)
        for word in words:
            checkMap = self.charsNo(word)
            check = True
            checkNo = 0
            for k, v in checkMap.items():
                check &= (k in can and v <= can[k])
                checkNo += v
            if check:
                re += checkNo
        return re

    def charsNo(self, ss):
        map = {}
        for s in ss:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        return map


if __name__ == '__main__':
    print(Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
