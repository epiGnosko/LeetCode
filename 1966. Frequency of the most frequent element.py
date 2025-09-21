class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start = 0
        window_sum = 0
        ans = 1
        for end in range(len(nums)):
            window_sum += nums[end]
            while nums[end] * (end - start + 1) - window_sum > k:
                window_sum -= nums[start]
                start += 1
            ans = max(ans, end - start + 1)
        return ans