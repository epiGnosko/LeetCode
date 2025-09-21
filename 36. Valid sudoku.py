class Solution:    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{},{},{},{},{},{},{},{},{}]
        cols = [{},{},{},{},{},{},{},{},{}]
        grid = [{},{},{},{},{},{},{},{},{}]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(c//3)*3 + r//3]:
                    return False
                rows[r][board[r][c]] = 1
                cols[c][board[r][c]] = 1
                grid[((c//3)*3 + r//3)][board[r][c]] = 1
                    
        return True