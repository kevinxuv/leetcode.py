#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = curent_node = ListNode(0)
        carry = 0
        while True:
            v1, v2 = 0, 0
            if l1 is not None:
                v1 = l1.val
            if l2 is not None:
                v2 = l2.val
            s = v1 + v2 + carry
            carry = int(s / 10)
            curent_node.next = ListNode(s % 10)
            curent_node = curent_node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is None and l2 is None:
                break
        if carry > 0:
            curent_node.next = ListNode(carry)

        return dummy_node.next
# @lc code=end
