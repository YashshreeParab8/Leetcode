# Q7 reverse integer
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        rev = rev * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev