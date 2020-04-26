#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#
from queue import PriorityQueue
from typing import List
# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.res = self.nums[-k:]

    def add(self, val: int) -> int:
        # print(self.res)
        if len(self.res) < self.k:
            self.res.append(val)
            self.res.sort()
            if len(self.res) == self.k:
                return self.res[0]
            return None
        else:
            if val >= self.res[0]:
                self.res.pop(0)
                self.res.append(val)
                self.res.sort()
            return self.res[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end


test_cases = {3: 4, 5: 5, 10: 5, 9: 8, 4: 8}

if __name__ == '__main__':
    s = KthLargest(3, [4, 5, 8, 2])
    for val, expected in test_cases.items():
        r = s.add(val)
        try:
            assert r == expected
        except:
            print(val, expected, 'fail: {}'.format(r))
