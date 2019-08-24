from random import randint
board = []
for x in range(10):
    board.append(["*"] * 10)


def print_board(board):
    for row in board:
        print((" ").join(row))




def random_row(board):
    return randint(0, len(board))


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row,"Simple Battleship!", ship_col, sep="")
print()
print_board(board)
for turn in range(15):
    print("Turn", turn+1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Good job, battleship was sank!")
        break
    else:
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
            print("Sorry, not in the range.")
        elif (board[guess_row][guess_col] == "X"):
            print("It was guessed already.")
        else:
            print("Missed!! Try again!")
            board[guess_row][guess_col] = "X"
    if turn == 15:
        print("Game Over")
    turn = + 1
    print_board(board)
