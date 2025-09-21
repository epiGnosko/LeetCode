class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [
            ["","",""],
            ["","",""],
            ["","",""],
        ]
        for i in range(len(moves)):
            if i % 2 == 0:
                grid[moves[i][0]][moves[i][1]] = "X"
            else:
                grid[moves[i][0]][moves[i][1]] = "O"

        rowcount_X = [0,0,0]
        colcount_X = [0,0,0]
        rowcount_O = [0,0,0]
        colcount_O = [0,0,0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "X":
                    rowcount_X[row] += 1
                    colcount_X[col] += 1
                elif grid[row][col] == "O":
                    rowcount_O[row] += 1
                    colcount_O[col] += 1
        for i in rowcount_X:
            if i == 3:
                return "A"
        for i in colcount_X:
            if i == 3:
                return "A"
        for i in rowcount_O:
            if i == 3:
                return "B"
        for i in colcount_O:
            if i == 3:
                return "B"
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            if grid[1][1] == "X":
                return "A"
            elif grid[1][1] == "O":
                return "B"
        if grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2]:
            if grid[1][1] == "X":
                return "A"
            elif grid[1][1] == "O":
                return "B"
        for i in grid:
            for j in i:
                if j == "":
                    return "Pending"
        return "Draw"