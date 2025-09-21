class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        count2 = {}
        for x in nums1:
            if x not in count1:
                count1[x] = 1
            else:
                count1[x] += 1
        for x in nums2:
            if x not in count2:
                count2[x] = 1
            else:
                count2[x] += 1
        ans = []
        for x in count1:
            if x in count2:
                ans.append(x)
        return ans