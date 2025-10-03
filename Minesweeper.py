import random

def create_board(size, bombs):
    board = [[" " for _ in range(size)] for _ in range(size)]
    bomb_positions = random.sample(range(size*size), bombs)
    for pos in bomb_positions:
        row, col = divmod(pos, size)
        board[row][col] = "B"
    return board

def get_adjacent_bombs(board, row, col):
    size = len(board)
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < size and 0 <= j < size and board[i][j] == "B":
                count += 1
    return count

def play_minesweeper(size=5, bombs=5):
    hidden_board = create_board(size, bombs)
    display_board = [["*" for _ in range(size)] for _ in range(size)]
    revealed = 0

    while True:
        for row in display_board:
            print(" ".join(row))
        
        try:
            r = int(input("Enter row (0-{}): ".format(size-1)))
            c = int(input("Enter col (0-{}): ".format(size-1)))
        except ValueError:
            print("⚠️ Invalid input.")
            continue

        if hidden_board[r][c] == "B":
            print("💥 BOOM! You hit a bomb. Game Over!")
            break
        else:
            bombs_near = get_adjacent_bombs(hidden_board, r, c)
            display_board[r][c] = str(bombs_near)
            revealed += 1

            if revealed == size*size - bombs:
                print("🎉 Congratulations! You cleared the board!")
                break

if __name__ == "__main__":
    play_minesweeper()
