def valid_sudoku(board):
    for row in board:
        if len(set(row)) != 9:
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[r+i][c+j])
            if len(set(subgrid)) != 9:
                return False

    return True


sample_board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

if valid_sudoku(sample_board):
    print("✅ Valid Sudoku!")
else:
    print("❌ Invalid Sudoku!")
