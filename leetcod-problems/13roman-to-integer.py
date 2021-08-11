class Solution:
    def romanToInt(self, s: str) -> int:
        intList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        re = 0
        for i in range(len(intList)):
            while s.startswith(strList[i]):
                re += intList[i]
                s = s[len(strList[i]):]

        return re
