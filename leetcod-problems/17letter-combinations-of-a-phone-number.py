from typing import List

dic = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations_(self, digits: str) -> List[str]:
        if digits == '': return []
        re = [""]
        for i in digits:
            re = [pre + sub for pre in re for sub in dic[i]]
        return re

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []

        mid = [[] for _ in range(len(digits) + 1)]
        mid[0].append("")
        for i in range(1, len(digits) + 1):
            last = mid[i - 1]
            now = dic[digits[i - 1]]
            for j in last:
                for n in now:
                    mid[i].append(j + n)
        return mid[len(digits)]


if __name__ == "__main__":
    print(Solution().letterCombinations("765476"))
