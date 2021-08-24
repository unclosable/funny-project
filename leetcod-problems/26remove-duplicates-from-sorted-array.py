from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        re = 0
        for i in range(len(nums)):
            if nums[re] != nums[i]:
                re += 1
                nums[re] = nums[i]
        re += 1
        return re


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2, 2, 3, 5, 6, 6, 7, 8]))
