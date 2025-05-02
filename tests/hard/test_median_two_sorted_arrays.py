from typing import List

import pytest

from src.hard.median_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Basic odd total length
        ([1, 3], [2], 2.0),
        # Basic even total length
        ([1, 2], [3, 4], 2.5),
        # One empty array
        ([], [1], 1.0),
        ([2], [], 2.0),
        # Large difference in sizes
        ([0, 0, 0, 0], [5, 5, 5], 0.0),  # combined [0,0,0,0,5,5,5] median=0
        # Negative numbers
        ([-3, -1], [-2], -2.0),
        ([-5, -3, -1], [0, 2, 4], -0.5),
        # Duplicates
        ([1, 1, 1], [1, 1, 1], 1.0),
        ([1, 2, 3], [2, 3, 4], 2.5),
        # Uneven split
        ([1, 4, 7, 8], [2, 3], 3.5),
        ([1, 2], [3, 4, 5, 6, 7], 4.0),
    ],
)  # type: ignore[misc]
def test_find_median_sorted_arrays(
    nums1: List[int], nums2: List[int], expected: float
) -> None:
    result: float = Solution().find_median_sorted_arrays(nums1, nums2)
    assert pytest.approx(result, rel=1e-9) == expected
