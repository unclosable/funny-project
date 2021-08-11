import collections

from invoke import collection


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sco = [[None for i in range(len(s))] for m in range(numRows)]

        print(sco)
        x, y = 0, 0
        for i in s:
            print(f'{x} - {y}   {i}')
            sco[x][y] = i

            if not y % numRows == 0:
                y += 1

            if x < numRows - 1 and y % numRows == 0:
                x += 1
            elif x > 0 and not y % numRows == 0:
                x -= 1
            elif x == numRows - 1:
                y += 1
                x -= 1
                x = 0 if x < 0 else x
            # else:
            #     y += 1
        re = []
        for l in sco:
            for m in l:
                if m: re.append(m)

        return "".join(re)


if __name__ == "__main__":
    print(Solution().convert("ABC", 1))
