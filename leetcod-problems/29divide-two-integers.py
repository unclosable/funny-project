import math
import sys


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend if -dividend < (math.pow(2, 31) - 1) else int(math.pow(2, 31) - 1)
        if dividend == 0:
            return 0

        sign = 1
        _dividend, _divisor = dividend, divisor
        if (_dividend > 0 and _divisor < 0) or (_dividend < 0 and _divisor > 0):
            sign = -1

        if _divisor < 0: _divisor = -_divisor
        if _dividend < 0: _dividend = -_dividend

        num = self.div(_dividend, _divisor)
        return num if sign == 1 else -num

    def div(self, a: int, b: int) -> int:
        if a < b: return 0
        count = 1
        tb = b
        while (tb + tb) <= a:
            count = count + count
            tb = tb + tb
        return count + self.div(a - tb, b)


if __name__ == '__main__':
    print(Solution().divide(-2147483648,
                            -1))

    print(sys.maxsize)
