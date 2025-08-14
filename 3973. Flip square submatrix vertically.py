class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k//2):
            for j in range(k):  
                temp = grid[x+i][y + j]
                grid[x+i][y + j] = grid[x+k-i-1][y + j]
                grid[x+k-i-1][y + j] = temp
        return grid