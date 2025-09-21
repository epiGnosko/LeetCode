class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        present = set()
        for i in nums:
            if i not in present:
                present.add(i)
            else:
                return True
        return False