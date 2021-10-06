from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.backtrack(board, 0, ans)
        return ans

    def backtrack(self, board, row, ans):
        if row == len(board):
            ans.append(["".join(r) for r in board])
            return
        col_size = len(board[0])
        for col in range(col_size):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1, ans)
            board[row][col] = '.'

    def is_valid(self, board, row, col):
        n = len(board)
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))

