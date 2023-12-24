class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        submatrix = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == '.':
                    continue
                if (board[row][column] in rows[row] or
                   board[row][column] in columns[column] or
                   board[row][column] in submatrix[row//3,column//3]):
                   return False
                columns[column].add(board[row][column])
                rows[row].add(board[row][column])
                submatrix[row//3, column//3].add(board[row][column])
        return True