# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise
from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(set(counts.values())) == len(counts)