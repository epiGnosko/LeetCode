class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min = nums[0]
        max = nums[0]
        for i in nums:
            if i < min:
                min = i
            if i > max:
                max = i
        return (max - min) * k