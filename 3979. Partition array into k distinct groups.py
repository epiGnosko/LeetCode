class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        groups = len(nums) / k
        
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for i in count:
            if count[i] > groups:
                return False
        return True