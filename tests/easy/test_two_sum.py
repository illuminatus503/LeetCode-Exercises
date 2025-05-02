import pytest

from src.easy.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # LeetCode examples
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        # additional cases
        ([-3, 4, 3, 90], 0, [0, 2]),  # negative + positive
        ([1, 2, 3, 4, 5], 9, [3, 4]),  # last two
        ([0, 4, 3, 0], 0, [0, 3]),  # zeros
        ([1, 5, 5, 7], 10, [1, 2]),  # duplicate values
        ([5, 75, 25], 100, [1, 2]),  # small array
        ([2, -1, 1, -2], 0, [1, 2]),  # mixing signs
        ([1, 2], 3, [0, 1]),  # minimal size
        ([1, 1], 2, [0, 1]),  # two same minimal elements
    ],
)  # type: ignore[misc]
def test_two_sum_various(nums: list[int], target: int, expected: list[int]) -> None:
    solution: Solution = Solution()
    result: list[int] = solution.twoSum(nums, target)  # type: ignore[assignment]
    assert result is not None
    assert sorted(result) == sorted(expected)


def test_two_sum_no_solution_returns_none() -> None:
    solution: Solution = Solution()
    no_solution: None = solution.twoSum([1, 2, 3], 7)  # type: ignore[assignment]
    assert no_solution is None


def test_two_sum_unique_pair_powers_of_two() -> None:
    solution: Solution = Solution()

    # Build an array of powers of two so each pair sum is unique
    nums: list[int] = [1 << k for k in range(20)]  # [1, 2, 4, ..., 524288]

    # choose elements 8 and 128
    i: int = 3
    j: int = 7

    target: int = nums[i] + nums[j]
    result: list[int] = solution.twoSum(nums, target)  # type: ignore[assignment]

    # Verify the exact unique indices
    assert result is not None
    assert (result == [i, j]) or (result == [j, i])


def test_two_sum_performance_on_powers_of_two() -> None:
    solution: Solution = Solution()
    nums: list[int] = [1 << k for k in range(16)]
    # worst-case: the two largest at the end
    last_index: int = len(nums) - 1
    second_last: int = len(nums) - 2
    target: int = nums[last_index] + nums[second_last]
    result: list[int] = solution.twoSum(nums, target)  # type: ignore[assignment]
    assert result is not None
    assert (result == [second_last, last_index]) or (
        result == [last_index, second_last]
    )
