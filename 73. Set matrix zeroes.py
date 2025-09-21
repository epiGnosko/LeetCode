class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    found = True
                    zeroes.append((r,c))


        for zero in zeroes:
            x,y = zero
            for r in range(len(matrix)):
                matrix[r][y] = 0
            for c in range(len(matrix[0])):
                matrix[x][c] = 0