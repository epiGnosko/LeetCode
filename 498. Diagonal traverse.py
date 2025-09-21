class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) 
        n = len(matrix[0])
        out = []

        r = c = 0

        for _ in range(m * n):
            out.append(matrix[r][c])

            if (r + c) % 2 == 0:
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1

        return out