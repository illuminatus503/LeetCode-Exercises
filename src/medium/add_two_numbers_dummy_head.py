"""Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

----

Example 1:
2 -> 4 -> 3
5 -> 6 -> 4
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

----

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

----

"""

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional[ListNode] = None) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next_node


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        aux_l1: Optional[ListNode] = l1
        aux_l2: Optional[ListNode] = l2

        # Dummy head, with value 0
        dummy: ListNode = ListNode()
        current: ListNode = dummy
        carry: int = 0

        while aux_l1 or aux_l2:
            sum_value: int = carry

            if aux_l1:
                sum_value += aux_l1.val
                aux_l1 = aux_l1.next

            if aux_l2:
                sum_value += aux_l2.val
                aux_l2 = aux_l2.next

            # Trace the digit sum value and the carry.
            # Then, continue: add a carry node if needed.
            carry = sum_value // 10
            current.next = ListNode(
                val=sum_value % 10,
                next_node=ListNode(carry) if carry > 0 else None,
            )
            current = current.next

        return dummy.next
