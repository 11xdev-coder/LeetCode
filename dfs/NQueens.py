class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols, diag1, diag2 = set(), set(), set()
        result, board = [], []

        def dfs(row):
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board.append(col)
                dfs(row+1)
                board.pop()
                diag2.remove(row + col)
                diag1.remove(row - col)
                cols.remove(col)

        dfs(0)
        ans = []
        for b in result:
            current_board = []
            for target_col in b:
                row = []
                for num in range(n):
                    if num == target_col:
                        row.append('Q')
                    else:
                        row.append('.')
                current_board.append("".join(row))
            ans.append(current_board[:])
        
        return ans
