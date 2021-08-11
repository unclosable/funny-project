import math


class Solution:
    def reverse(self, x: int) -> int:

        reint = 0
        _x = x
        while _x != 0:
            reint = reint * 10 + math.fmod(_x, 10)
            _x = int(_x / 10)
        if reint > 2 ** 31 - 1 or reint <= -2 ** 31:
            return 0

        return int(reint)


if __name__ == '__main__':
    print(Solution().reverse(-12475892479832758947983201))
    # print(1534236469>2 ** 31)
#