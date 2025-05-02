"""Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate
characters.

----

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.

----

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

from typing import Dict


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        char_map: Dict[str, int] = {}

        # Use a sliding window to calculate the max. length
        # substring in the string.
        i: int = 0
        max_length: int = 0

        for j in range(0, len(s)):
            # If the character already exists in the map (that is, is inside the
            # prev. window), move the window forward.
            if s[j] in char_map and char_map[s[j]] >= i:
                i = char_map[s[j]] + 1

            # Otherwise, simply update the last appearance of s[j] and the length
            # of the window
            char_map[s[j]] = j
            max_length = max(max_length, j - i + 1)

        return max_length
