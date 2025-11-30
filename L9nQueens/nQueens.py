def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col, n):
    if col == n:
        print("Solution Found: ")
        printboard(board)
        return True
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col+1, n):
                return True
            board[i][col] = 0
    return False

def printboard(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    n = int(input("Enter the number of Queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve(board, 0, n):
        print("Solution not found")