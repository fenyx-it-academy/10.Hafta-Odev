#WEEK10
from random import randint


board = []

for i in range(0,5):
    board.append(["0"] *5)

def print_board(board):
    for i in board:
        print(" ").join(row)

#Add your code below!
def random_row(board):
    return randint(0, len(board)-1)#the reason we do -1 here is that everything other than
                                  #len starts wfrom 0, while len starts from 1, thats why
def random_col(board):
    return randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

#Add your code below!

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col: "))

print(ship_row)
print(ship_col)

#Everything from here on should go
#Write your code below
for turn in range(4):
    print("Turn"), turn + 1
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
    else:
        if guess_row > range(5) or guess_col > range(5):
            print("Oops, that is not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guess that one already.")
        else:
            print("You missed my battleship.")
            board[guess_row, guess_col] = "X"
            if turn == 3:
                print("Game Over!")
            #print(turn+1) here!
        print_board(board)







###############
board = []

from random import randint

for x in range(7):
    board.append(['O'] * 10)


def print_board(board):
    for List in board:
        print
        " ".join(List)


# setting up shipA
shipA1 = [randint(1, 7), randint(1, 10)]  # use line for debugging
shipA2v = [[shipA1[0] + 1, shipA1[1]], [shipA1[0], shipA1[1] + 1]]
shipA2 = shipA2v[randint(0, 1)]  # use line for debugging
# setting up shipA2
if shipA1[0] == 7 and shipA2 == shipA2v[0]:
    shipA2 = [shipA1[0] - 1, shipA1[1]]
if shipA1[1] == 10 and shipA2 == shipA2v[1]:
    shipA2 = [shipA1[0], shipA1[1] - 1]
shipA3 = []
if shipA2[0] == shipA1[0] + 1 and shipA2[0] != 7:
    shipA3 = [shipA2[0] + 1, shipA2[1]]
elif shipA2[0] == shipA1[0] - 1:
    shipA3 = [shipA1[0] - 2, shipA2[1]]
if shipA2[1] == shipA1[1] + 1 and shipA2[1] != 10:
    shipA3 = [shipA2[0], shipA2[1] + 1]
elif shipA2[1] == shipA1[1] + 1 and shipA2[1] == 10:
    shipA3 = [shipA2[0], shipA1[1] - 1]
if shipA2[0] == shipA1[0] + 1 and shipA2[0] == 7:
    shipA3 = [shipA1[0] - 1, shipA1[1]]
if shipA1[1] == 10 and shipA2[1] == shipA1[1] - 1:
    shipA3 = [shipA1[0], shipA2[1] - 1]


# setting up shipB
def shipB_setup():
    shipB1 = [randint(1, 7), randint(1, 10)]
    shipB2v = [[shipB1[0] + 1, shipB1[1]], [shipB1[0], shipB1[1] + 1]]
    shipB2 = shipB2v[randint(0, 1)]
    if shipB1[0] == 7 and shipB2 == shipB2v[0]:
        shipB2 = [shipB1[0] - 1, shipB1[1]]
    if shipB1[1] == 10 and shipB2 == shipB2v[1]:
        shipB2 = [shipB1[0], shipB1[1] - 1]
    shipB = [shipB1, shipB2]
    return shipB


def shipC_setup():
    shipC = [randint(1, 7), randint(1, 10)]
    return shipC


shipA = [shipA1, shipA2, shipA3]

shipB = shipB_setup()

shipC = shipC_setup()

# check to see if ships A,and B overlap
for point in shipB:  # still producing duplicates I think <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if point in shipA:
        shipB = []
    if shipB == []:
        shipB = shipB_setup()
# checks if ship C overlaps shipA and shipB
if shipC in shipA or shipC in shipB:
    shipC = shipC_setup()

# ================DEBUGGING LINES===============
print
shipA
print
shipB
print
shipC
# =============================================

guesses = 10

print
"Lets play Battleship!\nThere are 3 different ships all are one wide.\nShipA is 3 tiles long.\nShipB is 2 tiles long.\nShipC is 1 tile long."
print
"You will have " + str(guesses) + " guesses to get the three ships."

print_board(board)

shipAcount = 0
shipBcount = 0
shipCcount = 0
both = []

while guesses > 0:
    print
    "Guesses: " + str(int(guesses))
    if shipAcount == 3 and shipBcount == 2 and shipCcount == 1:
        print
        "All ships have been sunk. You win!"
        break
    guess_row = int(raw_input("Guess a row (1-7): "))
    if guess_row > 7 or guess_row < 1:
        print
        "That row is not in range. Please guess a row 1-7"
    else:
        guess_col = int(raw_input("Guess a col (1-10): "))
        if guess_col > 10 or guess_col < 1:
            print
            "That column is not in range. Please guess a column 1-10"
        else:
            if board[guess_row - 1][guess_col - 1] == "X" or board[guess_row - 1][guess_col - 1] == "C" or
                    board[guess_row - 1][guess_col - 1] == "B" or board[guess_row - 1][guess_col - 1] == "A":
                print
                "You've already guessed there! Guess again."
            else:
                if [guess_row, guess_col] == shipC:
                    print
                    "You've sunk shipC! Marked with a 'C'"
                    board[guess_row - 1][guess_col - 1] = "C"
                    shipCcount = 1
                    print_board(board)
                for point in shipB:
                    if [guess_row, guess_col] == point:
                        board[guess_row - 1][guess_col - 1] = "B"
                        shipBcount += 1
                        if shipBcount == 2:
                            print
                            "You sunk shipB!"
                            print_board(board)
                        else:
                            print
                            "You hit shipB! Marked with a 'B'"
                            print_board(board)
                for point in shipA:
                    if [guess_row, guess_col] == point:
                        board[guess_row - 1][guess_col - 1] = "A"
                        shipAcount += 1
                        if shipAcount == 3:
                            print
                            "You sunk shipA!"
                            print_board(board)
                        else:
                            print
                            "You hit shipA! Marked with an 'A'"
                            print_board(board)
                for point in shipB:
                    both.append(point)
                for point in shipA:
                    both.append(point)
                both.append(shipC)
                if [guess_row, guess_col] not in both:
                    print
                    "You missed. Misses are marked with an 'X'"
                    board[guess_row - 1][guess_col - 1] = "X"
                    print_board(board)
                    guesses -= 1

if guesses == 0:
    print
    "Out of guesses. You lose."
