import pytest

from src.medium.longest_substring_without_rep_char import Solution


def test_return_type() -> None:
    """
    Ensure the method returns an integer for valid string inputs.
    """
    result = Solution().length_of_longest_substring("abc")
    assert isinstance(result, int)


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", 0),                 # Empty string (constraint: length 0)
        ("abcabcbb", 3),         # Example 1: "abc", length 3
        ("bbbbb", 1),            # Example 2: "b", length 1
        ("pwwkew", 3),           # Example 3: "wke", length 3
        ("abcdef", 6),           # All unique
        ("abba", 2),             # Repetition with backtracking
        ("tmmzuxt", 5),          # Mixed repeats
        ("你好你好", 2),          # Unicode characters
        ("aあa", 2),             # Mixed ASCII and non-ASCII
    ]
)
def test_various_cases(input_str: str, expected: int) -> None:
    """
    Test multiple scenarios comparing to expected longest substring lengths.
    """
    assert Solution().length_of_longest_substring(input_str) == expected


def test_max_length_performance() -> None:
    """
    Performance sanity check on maximum length constraint.
    Constraint: 0 <= s.length <= 5 * 10**4
    Test with s.length == 50000, all unique characters.
    """
    # generate 50000 unique characters by cycling through unicode BMP range
    s = ''.join(chr(0x4E00 + (i % 1000)) for i in range(50000))
    assert len(s) == 50000
    assert Solution().length_of_longest_substring(s) == 1000
