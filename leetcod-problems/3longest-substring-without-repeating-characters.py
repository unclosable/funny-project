class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, ed = 0, 0
        max = 0
        dic = {}
        while ed < len(s):
            i = s[ed]
            print(s[st:ed])
            if i in dic:
                st = dic[i] if dic[i] > st else st
            max = max if ed - st + 1 < max else ed - st + 1
            dic[i] = ed + 1

            ed += 1
        return max

    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxx = 1
        flg = True
        for i in range(len(s)):
            re = 1
            for j in range(i + 1, len(s)):
                # print(f'{s[j]} - {s[i:j]}')
                if s[j] not in s[i:j]:
                    re += 1
                else:
                    flg = False
                    break

            if re > maxx:
                maxx = re
        return len(s) if flg else maxx


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("pwwkew"))

    # print('as'[0:2])
