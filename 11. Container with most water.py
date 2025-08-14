class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1
        maxarea = 0
        while start < end:
            area = min(height[start],height[end]) * (end - start)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            if maxarea < area:
                maxarea = area
        return maxarea
