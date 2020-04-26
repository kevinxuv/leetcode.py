#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = {}
        # for num in nums:
        #     if num not in counts.keys():
        #         counts[num] = 1
        #     else:
        #         counts[num] += 1
        # for num, count in counts.items():
        #     if count > len(nums)/2:
        #         return num

        # count duplicate num till count > n/2
        nums = sorted(nums)
        n = len(nums)
        count = 1
        for i in range(0, n):
            tmp = nums[i]
            if i + 1 < n and nums[i + 1] == tmp:
                count += 1
            else:
                count = 1
            if count > n/2:
                return nums[i]
# @lc code=end

