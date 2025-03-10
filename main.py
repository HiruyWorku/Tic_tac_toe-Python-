def displayBoard(B):
    boardIndent = "   "
    print("\n")
    for row in range(len(B)-1,-1,-1):
        print(end=boardIndent)
        for col in range(len(B[row])-1):
            print(' ' + str(B[row][col]), end=' |')
        print(' ' + str(B[row][len(B[row])-1]) + ' ')
        if row > 0:
            print(end=boardIndent)
            for col in range(len(B[row])-1):
                print('-' + '-' * len(str(B[row][col])), end='-+')
            print('-' + '-' * len(str(B[row][len(B[row])-1])) + '-')
    print("\n")


def check_winner(board, symbol):
    """Check rows, columns, and diagonals for a win."""
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = [('X', "Player 1"), ('O', "Player 2")]
    
    print("Welcome to Tic-Tac-Toe!")
    displayBoard(board)

    for turn in range(9):  
        symbol, player = players[turn % 2]
        while True:
            move = input(f"{player} ({symbol}), enter your move (x,y) [1-3,1-3]: ")
            try:
                x, y = map(int, move.split(','))
                if 1 <= x <= 3 and 1 <= y <= 3 and board[y-1][x-1] == ' ':
                    board[y-1][x-1] = symbol
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input format. Enter as x,y (e.g., 2,3).")
        
        displayBoard(board)

        if check_winner(board, symbol):
            print(f"🎉 {player} wins! 🎉")
            return
        
    print("It's a draw! 🤝")


if __name__ == "__main__":
    tic_tac_toe()

