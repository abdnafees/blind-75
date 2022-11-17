"""
Solution for the famous Two Sum problem in Python from LeetCode.
Details from LeetCode:
Runtime: 126 ms, faster than 66.15% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 54.60% of Python3 online submissions for Two Sum.

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        dict_nums = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict_nums:
                return [dict_nums[diff], i]
            else:
                dict_nums[n] = i
        return output
