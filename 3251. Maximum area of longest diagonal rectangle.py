class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = dimensions[0][0]**2 + dimensions[0][1]**2
        max_area = dimensions[0][0] * dimensions[0][1]
        for i in dimensions:
            diag_sq = i[0]**2 + i[1]**2
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = i[0] * i[1]
            elif diag_sq == max_diag_sq:
                max_area = max(max_area, i[0] * i[1])
        return max_area