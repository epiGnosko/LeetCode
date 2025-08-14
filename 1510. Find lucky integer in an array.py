class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        largestluckiest = -1
        for i in count:
            if count[i] == i and i > largestluckiest:
                largestluckiest = i
        return largestluckiest
        