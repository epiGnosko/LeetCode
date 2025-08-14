class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in record:
                return (record[complement], i)
            record[nums[i]] = i
        return (-1,-1)