class Solution:
    def intToRoman(self, num: int) -> str:
        intList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        re = ""
        for i in range(len(intList)):
            if num >= intList[i]:
                re += strList[i]
                num -= intList[i]

        return re
