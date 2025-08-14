class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        first = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return first

        def findLast(nums, target):
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        last = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]