class Solution {
public:
    bool isValid(vector<string>& board, int row, int col, int n) {
        for (int i = 0; i < row; i++) {
            int qCol = -1;
            for (int k = 0; k < n; k++)
                if (board[i][k] == 'Q')
                    qCol = k;
            if (qCol == col || abs(qCol - col) == abs(i - row))
                return false;
        }
        return true;
    }

    void solve(vector<vector<string>>& result, vector<string>& board, int row,
               int n) {
        if (row == n) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; ++col) {
            if (isValid(board, row, col, n)) {
                board[row][col] = 'Q';
                solve(result, board, row + 1, n);
                board[row][col] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));
        solve(result, board, 0, n);
        return result;
    }
};
