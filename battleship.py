from random import randint
from time import sleep

NUM_SHIPS = 8
NUM_ROWS = 10
NUM_COLS = 10


def random_row():
    return randint(0, NUM_ROWS - 1)


def random_col():
    return randint(0, NUM_COLS - 1)


def create_ships():
    ships = []
    for i in range(NUM_SHIPS):
        ship = (random_row(), random_col())
        while ship in ships:
            ship = (random_row(), random_col())
        ships.append(ship)
    return ships


def create_board():
    # 0: deniz, 1: gemi, 2: iska, 3: batmis gemi
    board = []
    for x in range(0, NUM_ROWS):
        board.append([0] * NUM_COLS)
    ships = create_ships()
    for ship in ships:
        board[ship[0]][ship[1]] = 1
    return board


def print_board(board, show_answer=False):
    print("   1 2 3 4 5 6 7 8 9 10")
    for i, row in enumerate(board):
        print("{:>2d} ".format(i + 1), end="")
        for cell in row:
            if cell == 0 or (cell == 1 and not show_answer):
                print('0', end="")
            elif cell == 2:
                print('X', end="")
            elif cell == 3 or (cell == 1 and show_answer):
                print('G', end="")
            print(' ', end="")
        print()


def main():
    print("BATTLESHIP")
    print("15 Attemps tp shoot")
    board = create_board()
    num_sunk_ships = 0

    for turn in range(15):
        print_board(board)
        print("Tur", turn + 1)
        guessed_row = int(input("Guess row: ")) - 1
        guessed_col = int(input("Guess column: ")) - 1
        if guessed_row < 0 or guessed_row >= NUM_ROWS or guessed_col < 0 or guessed_col >= NUM_COLS:
            print("Out of ocean.")
            continue
        guessed_cell = board[guessed_row][guessed_col]
        if guessed_cell == 0:
            print("you missed!")
            board[guessed_row][guessed_col] = 2
        elif guessed_cell == 1:
            board[guessed_row][guessed_col] = 3
            num_sunk_ships += 1
            print("You hitted the ship!".format(num_sunk_ships))
            if num_sunk_ships == NUM_SHIPS:
                print_board(board)
                print(
                    "Congrats. You won the game".format(NUM_SHIPS))
                break
        elif guessed_cell == 2 or guessed_cell == 3:
            print("You shooted there.")
    print_board(board, show_answer=True)
    print("Game over!")


if __name__ == "__main__":
    main()
