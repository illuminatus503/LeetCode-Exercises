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

        solution: ListNode = ListNode()
        aux_solution: ListNode = solution

        while aux_l1 or aux_l2:
            sum_value: int = aux_solution.val

            if aux_l1:
                sum_value += aux_l1.val
                aux_l1 = aux_l1.next

            if aux_l2:
                sum_value += aux_l2.val
                aux_l2 = aux_l2.next

            # Trace the digit sum value and the carry
            aux_solution.val = sum_value % 10
            aux_solution.next = ListNode(sum_value // 10)

            if aux_l1 or aux_l2:
                aux_solution = aux_solution.next

        # Remove the last digit if it is 0
        if aux_solution.next and aux_solution.next.val == 0:
            aux_solution.next = None

        # TODO: implement a dummy-head approach

        return solution
