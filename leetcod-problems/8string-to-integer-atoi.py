class Solution:
    def myAtoi(self, s: str) -> int:
        flg = '0987654321'
        readed = 0
        sed = False
        sub = False
        for i in s:
            if sed:
                if i not in flg:
                    break
                else:
                    res = readed * 10 + int(i)
                    if res > 2 ** 31 - 1:
                        return -2 ** 31 if sub else 2 ** 31 - 1
                    readed = res

            if not sed:
                if i in flg and i != 0:
                    readed = int(i)
                    sed = True
                elif i == '-':
                    sub = True
                    sed = True
                elif i == '+':
                    sed = True
                elif i != ' ':
                    break

        return -readed if sub else readed


if __name__ == '__main__':
    print(Solution().myAtoi('421'))
