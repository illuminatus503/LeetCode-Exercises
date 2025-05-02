"""Two Sum
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.

----

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

----

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
----

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import Dict, List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        to_index : Dict[int, int] = {}

        for i, number in enumerate(nums):
            # The answer is composed by two elements. So, 
            #   - number < target, or equivallently
            #   - remainder > 0 always.
            #
            # Calculate the remainder and see if n + remainder = target up 
            # to this point.
            remainder = target - number
            if remainder in to_index:
                return [to_index[remainder], i]

            # The remainder up to `target` is not in memory. Associate the 
            # current value to the `i` index.
            # There are no duplicated values in the array, because the answer
            # is unique.
            to_index[number] = i

        return None
