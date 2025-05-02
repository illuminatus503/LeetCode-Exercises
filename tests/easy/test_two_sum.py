import pytest
from src.easy.two_sum import Solution

@pytest.mark.parametrize("nums,target,expected", [
    # LeetCode examples
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),

    # additional cases
    ([-3, 4, 3, 90], 0, [0, 2]),          # negative + positive
    ([1, 2, 3, 4, 5], 9, [3, 4]),         # last two
    ([0, 4, 3, 0], 0, [0, 3]),            # zeros
    ([1, 5, 5, 7], 10, [1, 2]),           # duplicate values
    ([5, 75, 25], 100, [1, 2]),           # small array
    ([2, -1, 1, -2], 0, [1, 2]),          # mixing signs
    ([1, 2], 3, [0, 1]),                  # minimal size
    ([1, 1], 2, [0, 1]),                  # two same minimal elements
])
def test_two_sum_various(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted(expected)


def test_two_sum_no_solution_returns_none():
    solution = Solution()
    assert solution.twoSum([1, 2, 3], 7) is None


def test_two_sum_unique_pair_powers_of_two():
    solution = Solution()
    # Build an array of powers of two, so any sum of two distinct elements is unique
    nums = [1 << k for k in range(20)]  # [1,2,4,...,524288]
    i, j = 3, 7  # choose 8 and 128
    target = nums[i] + nums[j]
    result = solution.twoSum(nums, target)
    assert result == [i, j] or result == [j, i]


def test_two_sum_performance_on_powers_of_two():
    solution = Solution()
    nums = [1 << k for k in range(16)]
    # worst-case: last two
    target = nums[-1] + nums[-2]
    result = solution.twoSum(nums, target)
    assert result == [len(nums)-2, len(nums)-1] or result == [len(nums)-1, len(nums)-2]
