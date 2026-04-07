class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            inputset = set()
            for j in range(9):
                if board[i][j] !=".":
                    if board[i][j] not in inputset:
                        inputset.add(board[i][j])
                    else:
                        return False
        for i in range(9):
            inputset = set()
            for j in range(9):
                if board[j][i] !=".":
                    if board[j][i] not in inputset:
                        inputset.add(board[j][i])
                    else:
                        return False
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])







        return True
                