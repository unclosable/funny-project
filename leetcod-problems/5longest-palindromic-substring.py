import collections


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max, maxL, maxR = 0, 0, 0
        for i in range(len(s)):
            l = 1
            left = i - 1
            right = i + 1
            while left >= 0 and s[i] == s[left]:
                l += 1
                left -= 1
            while right < len(s) and s[i] == s[right]:
                l += 1
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                l += 2
                left -= 1
                right += 1
            if l > max:
                max = l
                maxL = left
                maxR = right
        return s[maxL + 1:maxR]


if __name__ == '__main__':
    print(Solution().longestPalindrome("bccccccb"))
