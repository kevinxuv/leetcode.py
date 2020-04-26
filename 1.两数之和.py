#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        nums_dict = {}
        for i in range(0, nums_len):
            r = target - nums[i]
            if r in nums_dict.keys() and nums_dict[r] != i:
                return [nums_dict[r], i]
            nums_dict[nums[i]] = i

        raise ValueError('No two sum solution')
# @lc code=end


if __name__ == "__main__":
    r = Solution().twoSum([2, 7, 11, 15], 9)
    print(r)
    assert [0, 1] == r
