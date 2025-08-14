# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        mid = (start + end) // 2
        while start < end:
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2 
        return mid
        