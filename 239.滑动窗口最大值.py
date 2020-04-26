#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # solution 1
        # if not nums:
        #     return []
        # res = []
        # for i, v in enumerate(nums):
        #     if i + k > len(nums):
        #         break
        #     m = max(nums[i:i+k])
        #     res.append(m)
        # return res

        # solution 2
        if not nums:
            return []
        window, res = [], []
        for i, v in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= v:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
# @lc code=end

test_cases = [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7])
]

if __name__ == '__main__':
    for case in test_cases:
        nums, k, expected = case
        res = []
        try:
            res = Solution().maxSlidingWindow(nums, k)
            assert res == expected
        except:
            print(case, 'fail: {}'.format(res))
