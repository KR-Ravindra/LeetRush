class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
# solution:
# -> so for each row, column and submatrix we need to check if the set has any duplicate numbers. Let us ignore the `.` in input and then include all the numbers in each row and column.
# -> how do we consider submatrices? - two ways, one predefine them (only works for this). second is every location(x,y) in 9*9 submatrix on integer division with 3, will always belong to one of 3*3 sub matrix - eg (4,4) in 9,9 => (1,1)
# -> so you just have to append each value into its respective submatrix[i//3,j//3] and check if value is repeating in that set
# way1:
        row = defaultdict(set)
        column = defaultdict(set)
        submatrix = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row[i]) or (board[i][j] in column[j]) or (board[i][j] in submatrix[(i//3,j//3)]):
                    return False
                row[i].add(board[i][j])
                column[j].add(board[i][j])
                submatrix[(i//3,j//3)].add(board[i][j])
        print(f"{row=} {column=} {submatrix=}")
        return True

# way2: manually building submatrices
        # rowscount = defaultdict(set)
        # columncount = defaultdict(set)


        # for i in range(len(board)):
        #     for j in range(len(board)):
        #         if board[i][j] == '.':
        #             continue
        #         if (board[i][j] in rowscount[i] or
        #             board[i][j] in columncount[j] ):
        #             return False
        #         rowscount[i].add(board[i][j])
        #         columncount[j].add(board[i][j])
        # submatrices=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        # for x,y in submatrices:  
        #     submatrix = set()              
        #     for i in range(x,x+3):
        #         for j in range(y,y+3):
        #             if board[i][j] == '.':
        #                 continue
        #             if (board[i][j] in submatrix):
        #                 return False
        #             submatrix.add(board[i][j])
        # return True