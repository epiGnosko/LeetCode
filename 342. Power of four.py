class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n & 11 == 0:
            n = n >> 2
        return n == 1
        