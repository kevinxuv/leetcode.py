#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = sorted(nums1 + nums2)
        num3_len = len(num3)
        if num3_len % 2 == 0:
            return float(num3[int(num3_len/2 - 1)] + num3[int(num3_len/2)])/2
        else:
            return float(num3[int(num3_len/2)])
# @lc code=end

