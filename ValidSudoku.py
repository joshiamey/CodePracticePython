
def isValidSudoku(board: list[list[str]]) -> bool:
    r,c = 9,9
    rowMap = [[False for x in range(c+1)] for y in range(r)]
    colMap = [[False for x in range(c+1)] for y in range(r)]
    # 9 subgrids 0 to 8
    subcel = [[False for x in range(c+1)] for y in range(r)]
    
    #iterate over the board    
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                continue
            
            val = int(board[i][j])
            col = j 
            row = i 
            cell_id = (row//3) * 3 + col//3
            # it this value is already present in same row
            # or col
            if rowMap[row][val]:
                return False 
            else:
                rowMap[row][val] = True
            
            if colMap[col][val]:
                return False 
            else:
                colMap[col][val] = True
            
            # if this value is present in same subgrid
            if subcel[cell_id][val]:
                return False 
            else:
                subcel[cell_id][val] = True
            
    return True
            
    
if __name__ == "__main__":
    board = [
             ["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]
             ]
    
    print(isValidSudoku(board))
    board = [
             ["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","4",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]
             ]
    
    print(isValidSudoku(board))