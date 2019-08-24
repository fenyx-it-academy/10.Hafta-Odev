"""
Deniz olarak varsayacagimiz 10x10'luk bir tablo olusturun (X-O-X oyununa benzer).
Bu tabloya 2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik gemiler yerlestirin.
Yerlestirdiginiz gemileri kullanici gormeyecek. Kullanicidan tablo uzerindeki herhangi bir noktaya hamlede bulunmasini isteyin.
Kullanicinin hamlesi gemilerin herhangi bir noktasina isabet ederse kullaniciya tablo uzerinde bunu gosterin.
Ayni sekilde bosa atis yaptiginda da kullaniciya tablo uzerinde bunu gosterin ve kullanicinin 5 sn boyunca hamle yapmasini engelleyin.
Kullanici daha once hamle yapmis oldugu bir noktaya tekrar hamlede bulunursa bunu engelleyin.
Kullaniciya toplamda 15 yanlis hamle hakki verin. Kullanici tum gemileri vurdugunda oyunu bitirin.
Oyunu mumkun oldugunca fonksiyonlar kullanarak yapmanizi istiyoruz.

BONUS(ISTEGE BAGLI): Yukaridaki versiyonda gemiler sabit. Oyunu her actigimizda gemilerin yeri degismiyor.
Isteyenler gemilerin random yerlestirildigi bir versiyonunu yapabilir.
⚔⚔⚔💣💣💣⚔🏹🏹🏹🏹🏹🛥🛥🛥⛴⛴⛴⛴⛴🚢🚢🚢🚨🚨🚨🚩🚥🚦💧💧💧💧💧
"""
import random
from time import sleep
gameStart = """
\t\t Let's Play Battleship
\t\t{}

Enter the row and column number where you want to add an '⛴'.
Row numbers and column numbers are between 0 - 9.

\t\t\t\t\t     0   1   2   3   4   5   6   7  8   9 \n
\t\t\t\t\t 0   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 1   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 2   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 3   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 4   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 5   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 6   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 7   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 8   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n
\t\t\t\t\t 9   💧  💧  💧  💧  💧  💧  💧  💧  💧  💧 \n


The game starts now\n""".format('-'*len(" Let's Play Battleship "))
print(gameStart)
board=[]
for i in range(10):
    board.append(["💧"]*10)
def print_board(board):
   for i in board:
       print("  ".join(i)) # make the board

game1 = [
[[0, 2], [1, 2], [2, 2], [3, 2]],
[[1, 5], [1, 6], [1, 7], [1, 8]],
[[3, 9], [4, 9], [5, 9]],
[[5, 6], [6, 6], [7, 6]],
[[9, 3], [9, 4]],
[[9, 8], [9, 9]],
[[6, 1]],
[[5, 4]]
]
game2 = [
[[1, 1], [1, 2], [1, 3], [1, 4]],
[[5, 3], [5, 4], [5, 5], [5, 6]],
[[7, 1], [8, 1], [9, 1]],
[[5, 8], [6, 8], [7, 8]],
[[1, 3], [1, 4]],
[[1, 7], [1, 8]],
[[9, 5]],
[[9, 9]]
]
game3 = [
[[3, 6], [3, 7], [3, 8], [3, 9]],
[[5, 4], [6, 4], [7, 4], [8, 4]],
[[4, 0], [5, 0], [6, 0]],
[[7, 7], [8, 9], [9, 9]],
[[1, 0], [1, 1]],
[[5, 5], [5, 7]],
[[1, 4]],
[[9, 0]]
]
game4 = [
[[0, 6], [0, 7], [0, 8], [0, 9]],
[[2, 2], [2, 3], [2, 4], [2, 5]],
[[2, 8], [3, 8], [4, 8]],
[[5, 0], [5, 1], [5, 2]],
[[7, 0], [8, 0]],
[[8, 5], [9, 5]],
[[6, 7]],
[[9, 9]]
]
game5 = [
[[0, 0], [1, 0], [2, 0], [3, 0]],
[[0, 9], [1, 9], [2, 9], [3, 9]],
[[2, 2], [3, 2], [4, 2]],
[[7, 3], [8, 3], [9, 3]],
[[1, 5], [2, 5]],
[[5, 5], [6, 5]],
[[9, 0]],
[[7, 7]]
]
game_choice=[game1,game2,game3,game4,game5] #put together the winlist
all_games=random.choice(game_choice)
#print(all_games)#if you want to see the selected game please uncomment this line
moves = []
right_moves=[]
right=1
while right<=15:
    try:
        print("Your " f'{right}.Right')
        # we received the coordinates with user input
        x = int(input('\nEnter a integar for ROW between "0,1,2,3,4,5,6,7,8,9": '))
        y = int(input('Enter a integar for COLUMN between "0,1,2,3,4,5,6,7,8,9": '))
        print('\n')
        sleep(3)       # 3 secon for waiting
        if 0 <= x <= 9 and 0 <= y <= 9:
            attack = [x,y]
            if attack in moves:
                print('!!!...Warning ... You did this attack  before \n')
                continue
            else:
                moves.append(attack)
                board[x][y] = 'X '
                #print(board[all_games[0][0][0]][all_games[0][0][1]])
                if attack in all_games[0]:
                    board[all_games[0][0][0]][all_games[0][0][1]] = '⛴'
                    board[all_games[0][1][0]][all_games[0][1][1]] = '⛴'
                    board[all_games[0][2][0]][all_games[0][2][1]] = '⛴'
                    board[all_games[0][3][0]][all_games[0][3][1]] = '⛴'
                    print('...BOOOOOOOOM...You find 1.Ship.......<<<<<<<\n')

                    right_moves.append(attack)
                    for i in all_games:  # When the correct movement is made, we have added the ship's locations to the list
                        moves.append(i)
                if attack in all_games[1]:
                    board[all_games[1][0][0]][all_games[1][0][1]] = '⛴'
                    board[all_games[1][1][0]][all_games[1][1][1]] = '⛴'
                    board[all_games[1][2][0]][all_games[1][2][1]] = '⛴'
                    board[all_games[1][3][0]][all_games[1][3][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)  # dd all points of game_lisst to the moves
                    print('...BOOOOOOOOM...You Found 2.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                if attack in all_games[2]:
                    board[all_games[2][0][0]][all_games[2][0][1]] = '⛴'
                    board[all_games[2][1][0]][all_games[2][1][1]] = '⛴'
                    board[all_games[2][2][0]][all_games[2][2][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 3.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                if attack in all_games[3]:
                    board[all_games[3][0][0]][all_games[3][0][1]] = '⛴'
                    board[all_games[3][1][0]][all_games[3][1][1]] = '⛴'
                    board[all_games[3][2][0]][all_games[3][2][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 4.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                if attack in all_games[4]:
                    board[all_games[4][0][0]][all_games[4][0][1]] = '⛴'
                    board[all_games[4][1][0]][all_games[4][1][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 5.Ship.......<<<<<<<\n')
                    right_moves.append(
                        attack)
                if attack in all_games[5]:
                    board[all_games[5][0][0]][all_games[5][0][1]] = '⛴'
                    board[all_games[5][1][0]][all_games[5][1][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 6.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                if attack in all_games[6]:
                    board[all_games[6][0][0]][all_games[6][0][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 7.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                if attack in all_games[7]:
                    board[all_games[7][0][0]][all_games[7][0][1]] = '⛴'
                    for i in all_games:
                        moves.append(i)
                    print('...BOOOOOOOOM...You Found 8.Ship.......<<<<<<<\n')
                    right_moves.append(attack)
                print_board(board)
                right += 1
        else:
            print('\n!!!...Please enter a number between :0,1,2,3,4,5,6,7,8,9\n')
            continue
        if len(right_moves) == 8:
            print('\nCongratulations You Won The Game')
            quit()
    except ValueError:
        print('Please enter a number between :0,1,2,3,4,5,6,7,8,9')
