class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def generator(arr: List[int], unusedindices: List[int]):
            if not unusedindices:
                perms.append(arr[:])
            else:
                for i in unusedindices:
                    new_unused = [j for j in unusedindices if j != i]
                    generator(arr + [nums[i]], new_unused)
        generator([], [i for i in range(len(nums))])
        return perms