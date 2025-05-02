# tests/medium/test_add_two_numbers_dummy_head.py

from typing import Optional

import pytest

from src.medium.add_two_numbers_dummy_head import ListNode, Solution


def list_to_listnode(values: list[int]) -> Optional[ListNode]:
    """Helper to build a reversed linked list from a Python list."""
    if not values:
        return None
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def listnode_to_list(node: Optional[ListNode]) -> list[int]:
    """Helper to unwrap a linked list into a Python list."""
    result: list[int] = []
    cur: Optional[ListNode] = node
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    return result


@pytest.mark.parametrize(  # type: ignore[misc]
    "l1_vals, l2_vals, expected_vals",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9], [0, 0, 1]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
    ],
)
def test_add_two_numbers_various(
    l1_vals: list[int], l2_vals: list[int], expected_vals: list[int]
) -> None:
    solution: Solution = Solution()
    l1: Optional[ListNode] = list_to_listnode(l1_vals)
    l2: Optional[ListNode] = list_to_listnode(l2_vals)
    result: Optional[ListNode] = solution.addTwoNumbers(l1, l2)
    assert result is not None
    assert listnode_to_list(result) == expected_vals


def test_add_two_numbers_carry_over_end() -> None:
    solution: Solution = Solution()
    node1: Optional[ListNode] = list_to_listnode([5])
    node2: Optional[ListNode] = list_to_listnode([5])
    result: Optional[ListNode] = solution.addTwoNumbers(node1, node2)
    assert result is not None
    assert listnode_to_list(result) == [0, 1]


def test_add_two_numbers_max_length_and_values() -> None:
    solution: Solution = Solution()
    l1_vals: list[int] = [9 if i % 2 == 0 else 0 for i in range(100)]
    l2_vals: list[int] = [0 if i % 2 == 0 else 9 for i in range(100)]
    l1: Optional[ListNode] = list_to_listnode(l1_vals)
    l2: Optional[ListNode] = list_to_listnode(l2_vals)
    result: Optional[ListNode] = solution.addTwoNumbers(l1, l2)
    assert result is not None
    out_vals: list[int] = listnode_to_list(result)
    assert all(0 <= v <= 9 for v in out_vals)
    assert len(out_vals) in (100, 101)


def test_add_two_numbers_no_leading_zeros() -> None:
    solution: Solution = Solution()
    zero: Optional[ListNode] = list_to_listnode([0])
    other: Optional[ListNode] = list_to_listnode([1, 2, 3])
    res1: Optional[ListNode] = solution.addTwoNumbers(zero, other)
    res2: Optional[ListNode] = solution.addTwoNumbers(other, zero)
    assert res1 is not None and res2 is not None
    assert listnode_to_list(res1) == [1, 2, 3]
    assert listnode_to_list(res2) == [1, 2, 3]
