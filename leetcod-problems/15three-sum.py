from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _nums = sorted(nums)
        l = len(_nums) - 1

        re = []

        if l < 2:
            return re
        for i in range(0, l):
            if i > 0 and _nums[i] == _nums[i - 1]:
                continue
            h, e = i + 1, l
            while h < e:
                add = _nums[i] + _nums[h] + _nums[e]
                if add == 0:
                    re.append([_nums[i], _nums[h], _nums[e]])
                    while h < l and _nums[h + 1] == _nums[h]:
                        h += 1
                    while e > i and _nums[e] == _nums[e - 1]:
                        e -= 1
                if add < 0:
                    h += 1
                else:
                    e -= 1
        return re


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
                              ))
