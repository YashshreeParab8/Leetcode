# Given an array nums containing n distinct numbers in the range [0, n],
#  return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        total = n * (n + 1) // 2
        arr_sum = sum(nums)
        
        return total - arr_sum
