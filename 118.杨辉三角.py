#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
import copy
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            row = []
            for j in range(1, int((i+1)/2) + 1):
                row.append(self.caculate(i, j))
            if i > 1:
                _row = copy.copy(row)
                if i % 2:
                    row.pop(int((i+1)/2) - 1)
                row.reverse()
                row = _row + row
            res.append(row)
        return res

    def caculate(self, row, column):
        if column == 1 or row == column:
            return 1
        return self.caculate(row - 1, column - 1) + self.caculate(row - 1, column)
# @lc code=end


if __name__ == '__main__':
    print(Solution().generate(5))
