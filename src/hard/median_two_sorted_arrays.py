"""Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median
of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

----

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

----

Constraints:
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -106 <= nums1[i], nums2[i] <= 106

"""

from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array for O(log(min(m,n))) complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m: int = len(nums1)
        n: int = len(nums2)
        half_len: int = (m + n + 1) // 2

        # Binary search bounds on nums1
        low: int = 0
        high: int = m
        while low <= high:
            i: int = (low + high) // 2
            j: int = half_len - i

            # Partition boundaries or infinities at edges
            A_left: float = float(nums1[i - 1]) if i > 0 else float("-inf")
            A_right: float = float(nums1[i]) if i < m else float("inf")
            B_left: float = float(nums2[j - 1]) if j > 0 else float("-inf")
            B_right: float = float(nums2[j]) if j < n else float("inf")

            # Correct partition if all lefts ≤ all rights
            if A_left <= B_right and B_left <= A_right:
                # Odd total length: median is max of left sides
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                # Even total length: median is average of middle two
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            # Adjust binary search
            if A_left > B_right:
                high = i - 1
            else:
                low = i + 1

        # If inputs are invalid, return infinity. This case is not reachable in this
        # setup

        return float("inf")  # pragma: no cover
