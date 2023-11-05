import time
start = time.time()

def print_solution(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    # Check if no Queen can attack in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check if no Queen can attack in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check if no Queen can attack in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All Queens are placed successfully, print the solution
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, n)
            board[row][col] = '.'  # Backtrack

def n_queens(n):
    if n <= 0:
        return []

    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

n = 4  # Change this to the desired N value
n_queens(n)

end = time.time()
print("\nExecution time is: {}ms".format((end-start)*10**3))