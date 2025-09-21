class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {
            0 : 0,
            1 : 0,
            2 : 0,
        }
        for i in nums:
            count[i] += 1
        index = 0
        for _ in range(count[0]):
            nums[index] = 0
            index += 1
        for _ in range(count[1]):
            nums[index] = 1
            index += 1
        for _ in range(count[2]):
            nums[index] = 2
            index += 1
            
    
        