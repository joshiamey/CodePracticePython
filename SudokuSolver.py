from pprint import pprint

def isPossible(board:list[list[str]],row,col,val) -> bool:
    
    # check if value present in the row:
    for c in range(9):
        if board[row][c] == val:
            return False         
    
    # check if value present in all the col:
    for r in range(9):
        if board[r][col] == val:
            return False 
        
    # check subgrids 
    subcell_r = (row//3) * 3
    subcell_c = (col//3) * 3
    
    for r in range(subcell_r,subcell_r + 3):
        for c in range(subcell_c,subcell_c + 3):
            if board[r][c] == val:
                return False 
            
    return True


def solveSudoku(board:list[list[str]]) -> bool:
    
    for i in range(9):
        for j in range(9):
            
            if board[i][j] == '.' or board[i][j] == '':
                # try all values from 1 to 9
                for val in range(1,10):
                    if isPossible(board,i,j,str(val)):
                        board[i][j] = str(val) 
                        if not solveSudoku(board) :
                            # backtrack and try other values
                            # by restoring dots
                            board[i][j] = '.'
                        else:
                            # return true for we have solved the puzzle
                            return True
                # Return false as we did not find and possible values
                # for this particular cell.
                return False

    # All the dots are filled 
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
    
    solveSudoku(board)
    
    pprint(board)
    