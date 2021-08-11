import collections


# TODO 动态规划
def firstMatch(s, p):
    return len(s) != 0 and s[:1] == p[:1] or p[:1] == '.'


def pr(re):
    print('----')
    for i in re:
        print(i)


class Solution:
    def _isMatch(self, s: str, p: str) -> bool:
        print(f's {s}  p {p}')
        if len(p) == 0:
            return len(s) == 0

        if len(p) >= 2 and p[1:2] == '*':
            return self.isMatch(s, p[2:]) or firstMatch(s, p) and self.isMatch(s[1:], p)
        else:
            return firstMatch(s, p) and self.isMatch(s[1:], p[1:])
        # return True

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        re = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        re[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                re[0][j] = re[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(f' {i}  {j}')
                pr(re)
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    re[i][j] = re[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        re[i][j] = re[i][j - 2] or re[i - 1][j]
                    else:
                        re[i][j] = re[i][j - 2]
        # print(re)
        return re[m][n]


if __name__ == '__main__':
    # print(Solution().isMatch("aaabcaab",
    #                          "a*b.a*b"))
    print(Solution().isMatch("aa",
                             "a*"))
    # print(True and False or True)
