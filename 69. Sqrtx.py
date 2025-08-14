class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        start = 0
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        return int((start + end) // 2)