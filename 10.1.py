from random import randint
from time import sleep

turn_counter = 0

board = []

print ("BATTLESHIP")
print ("15 ATTEMPTS TO SHOOT")
print
sleep(1)
for x in range(0, 10):
  board.append(["O"] * 10)

def print_board(board):
  table_row_counter = 1
  print ("  1 2 3 4 5 6 7 8 9 10")
  for row in board:
    print (str(table_row_counter) + " " + " ".join(row))
    table_row_counter += 1

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)


ship_row1 = random_row(board)
ship_col1 = random_col(board)

ship_row2 = random_row(board)
ship_col2 = random_col(board)

ship_row3 = random_row(board)
ship_col3 = random_row(board)

def control():
  global ship_row2
  global ship_col2


  if ship_row1 == ship_row2:
    ship_row2 = random_row(board)
    control()
  if ship_col1 == ship_col2:
    ship_col2 = random_row(board)


control()

print

for turn in range(15):
  turn_counter += 1
  print ("Tur", turn + 1)
  guess_row1 = int(input("Guess row : "))-1
  guess_col1 = int(input("Guess col : "))-1
  print

  if guess_row1 == ship_row1 and guess_col1 == ship_col1:
    print ("! You hit a ship!")
    print
    board[guess_row1][guess_col1] = ("G")
    print_board(board)
    ship_row1 = None
    ship_col1 = None
    break
  elif guess_row1 == ship_row2 and guess_col1 == ship_col2:
    print ("You hit a ship! ")
    print
    board[guess_row1][guess_col1] = ("G")
    print_board(board)
    ship_row2 = None
    ship_col2 = None
    break
  else:
    if guess_row1 not in range(10) or \
      guess_col1 not in range(10):
      print_board(board)
      print ("Out of the ocean.")
      print
    elif board[guess_row1][guess_col1] == "X":
      print_board(board)
      print( "You shooted there" )
      print
    else:
      board[guess_row1][guess_col1] = "X"
      print_board(board)
      print ("You missed!")
      print
    if turn == 14:
      board[ship_row1][ship_col1] = ("G")
      board[ship_row2][ship_col2] = ("G")
      sleep(1.5)
      print
      print
      print_board(board)
      print ("Game over")

for turn in range (turn_counter,4):
  print
  print ("Tur", turn + 1)
  guess_row2 = int(raw_input("Guess row: "))-1
  guess_col2 = int(raw_input("Guess column: "))-1

  if guess_row2 == ship_row1 and guess_col2 == ship_col1 or guess_row2 == ship_row2 and guess_col2 == ship_col2:
    board[guess_row2][guess_col2] = "G"
    print
    print_board(board)
    print ("Congrats, you sink the ships!")
    print
    break
  else:
    if guess_row2 not in range(11) or \
      guess_col2 not in range(11):
      print ("Out of ocean")
      print
    elif board[guess_row2][guess_col2] == "X":
      print ("Out of ocean")
      print
    elif guess_row2 == guess_row1 and guess_col2 == guess_col1:
      print ("You hitted that ship.")
      print
    else:
      print ("You missed!")
      print
      board[guess_row2][guess_col2] = ("X")
    print_board(board)
    if turn == 3:
      print ("Game over")