from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1len, n2len = len(nums1), len(nums2)
        totle = n1len + n2len

        n = 0

        last, flg = -1, -1

        n1flg, n2flg = 0, 0
        while n <= totle / 2:
            last = flg
            n1, n2 = nums1[n1flg] if n1flg < n1len else None, nums2[n2flg] if n2flg < n2len else None

            # print(f'{n1} {n2}')
            if isinstance(n1, int) and isinstance(n2, int) and n1 > n2:
                # if n1 > n2:
                flg = n2
                n2flg += 1
            elif isinstance(n1, int) and isinstance(n2, int) and n2 > n1:
                flg = n1
                n1flg += 1
            elif isinstance(n1, int):
                flg = n1
                n1flg += 1
            else:
                flg = n2
                n2flg += 1
            n += 1
        if totle % 2 == 0:
            re = (last + flg) / 2
        else:
            re = flg
        return re


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([2], []))
