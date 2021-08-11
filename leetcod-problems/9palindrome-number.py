import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        _x = x
        while _x != 0:
            res = res * 10 + math.fmod(_x, 10)
            _x = int(_x / 10)

        return res == x



