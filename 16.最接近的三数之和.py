#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)
        gaps = {}
        for i in range(0, nums_len):
            left, right = i + 1, nums_len - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                gap = abs(_sum - target)
                gaps[gap] = _sum
                if _sum == target:
                    return nums[i] + nums[left] + nums[right]
                elif _sum < target:
                    left += 1
                else:
                    right -= 1
        keys = sorted(gaps.keys())
        return gaps[keys[0]]
# @lc code=end

test_cases = [
    ([-1,2,1,-4], 1, 2)
]

if __name__ == '__main__':
    for case in test_cases:
        nums, target, expected = case
        r = Solution().threeSumClosest(nums, target)
        try:
            assert r == expected
            print(case, 'pass')
        except:
            print(case)
            print(r)
