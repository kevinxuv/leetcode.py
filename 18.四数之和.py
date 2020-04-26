#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums_len = len(nums)
        if nums_len < 4:
            return result

        nums.sort()
        for i in range(0, nums_len):
            if nums[i] > target and nums[i] >= 0:
                return result

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, nums_len):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = nums_len - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while(left < right and nums[left] == nums[left+1]):
                            left += 1
                        while(left < right and nums[right] == nums[right-1]):
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return result
# @lc code=end

test_cases = [
    ([-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
    ([-1,0,1,2,-1,-4], -1, [[-4,0,1,2],[-1,-1,0,1]]),
    ([1,-2,-5,-4,-3,3,3,5], -11, [[-5,-4,-3,1]]),
    ([-1,-5,-5,-3,2,5,0,4], -7, [[-5,-5,-1,4],[-5,-3,-1,2]]),
    ([-1,0,-5,-2,-2,-4,0,1,-2], -9, [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]])
]

if __name__ == '__main__':
    for test_case in test_cases:
        nums, target, expected = test_case
        r = Solution().fourSum(nums, target)
        try:
            assert r == expected
            # print(test_case, 'pass')
        except:
            print(test_case, 'fail')
            print(expected)
            print(r)
