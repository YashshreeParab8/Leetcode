# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i