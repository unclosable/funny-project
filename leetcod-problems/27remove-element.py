from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        re = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[re] = nums[i]
                re += 1
        return re