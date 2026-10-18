# Given an integer n, find the digit that occurs least frequently in its decimal representation. 
# If multiple digits have the same frequency, choose the smallest digit. Return the chosen digit as an integer.
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        result = -1
        least = len(s) + 1

        for d in "0123456789":
            c = s.count(d)
            if c > 0 and c < least:
                least = c
                result = int(d)

        return result