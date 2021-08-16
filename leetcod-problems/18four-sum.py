import math
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        _nums = sorted(nums)
        l = len(_nums) - 1

        re = []
        for i in range(0, l):
            if i > 0 and _nums[i] == _nums[i - 1]:
                continue
            for j in range(i + 1, l):
                if j > i + 1 and _nums[j] == _nums[j - 1]:
                    continue
                h, e = j + 1, l
                while h < e:
                    add = _nums[i] + _nums[j] + _nums[h] + _nums[e]
                    if add == target:
                        re.append([_nums[i], _nums[j], _nums[h], _nums[e]])
                        while h < l and _nums[h + 1] == _nums[h]:
                            h += 1
                        while e > 0 and _nums[e - 1] == _nums[e]:
                            e -= 1

                    if add < target:
                        h += 1
                    else:
                        e -= 1
        return re


if __name__ == '__main__':
    print(Solution().fourSum([2, 2, 2, 2, 2],
                             8))
