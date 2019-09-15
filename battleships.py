from random import randint,choice
from time import sleep

def horizontal(unit):
    while True:
        ship = []
        coor = choice(all_coor)
        if coor[0] > 9 - unit:
            coor[0] = 9 - unit
        if coor not in ships:
            #to check whether 'coor' is besides other ship or not
            if [coor[0] + 1, coor[1]] not in ships:
                if [coor[0] - 1, coor[1]] not in ships:
                    if [coor[0], coor[1] + 1] not in ships:
                        if [coor[0], coor[1] - 1] not in ships:
                            ship.append(coor)
            
        for i in range(unit-1):
            coor = [coor[0] + 1] + [coor[1]]
            if coor not in ships:
                #to check whether 'coor' is besides other ship or not
                if [coor[0] + 1, coor[1]] not in ships:
                    if [coor[0] - 1, coor[1]] not in ships:
                        if [coor[0], coor[1] + 1] not in ships:
                            if [coor[0], coor[1] - 1] not in ships:
                                ship.append(coor)

        if len(ship) == unit:
            ships.extend(ship)
        else:
            continue
        return ships

def vertical(unit):
    while True:
        ship = []
        coor = choice(all_coor)
        if coor[1] > 9 - unit:
            coor[1] = 9 - unit
        if coor not in ships:
            #to check whether 'coor' is besides other ship or not
            if [coor[0] + 1, coor[1]] not in ships:
                if [coor[0] - 1, coor[1]] not in ships:
                    if [coor[0], coor[1] + 1] not in ships:
                        if [coor[0], coor[1] - 1] not in ships:
                            ship.append(coor)
            
        for i in range(unit-1):
            coor = [coor[0]] + [coor[1] + 1]
            if coor not in ships:
                #to check whether 'coor' is besides other ship or not
                if [coor[0] + 1, coor[1]] not in ships:
                    if [coor[0] - 1, coor[1]] not in ships:
                        if [coor[0], coor[1] + 1] not in ships:
                            if [coor[0], coor[1] - 1] not in ships:
                                ship.append(coor)

        if len(ship) == unit:
            ships.extend(ship)
        else:
            continue
        return ships

def deploy():
    #for ships which has 4 units
    counter = 0
    while True:
        mark = randint(0,1)
        if counter == 2:
            break

        elif mark == 0:
            horizontal(4)

        elif mark == 1:
            vertical(4)
        counter += 1
    #for ships which has 3 units
    counter = 0
    while True:
        mark = randint(0,1)
        if counter == 2:
            break

        elif mark == 0:
            horizontal(3)

        elif mark == 1:
            vertical(3)
        counter += 1
    #for ships which has 2 units
    counter = 0
    while True:
        mark = randint(0,1)
        if counter == 2:
            break

        elif mark == 0:
            horizontal(2)

        elif mark == 1:
            vertical(2)
        counter += 1
    #for ships which has 1 unit
    counter = 0
    while True:
        mark = randint(0,1)
        if counter == 2:
            break
        horizontal(1)
        counter += 1


def all_ships():
    for ship in ships:
        table[ship[0]][ship[1]] = "XX"
    return table

def print_table():
    for item in table:
        print("\n\t".expandtabs(20),*item)
    if time:
        sleep(1)
        
def coordinate():
    global y
    global x
    while True:
        y = input("\nPlease choose the y axis:")
        if y.isdigit() == False:
            print("Please enter number between 0 - 10.")
            time = False
            continue
        else:
            y = int(y)
        y = y - 1
        if y > 9 or y < 0:
            print("Please enter number between 0 - 10.")
            continue
        
        x = input("\nPlease choose the x axis:")
        if x.isdigit() == False:
            print("Please enter number between 0 - 10.")
            time = False
            continue
        else:
            x = int(x)
        x = x - 1
        if x > 9 or x < 0:
            print("Please enter number between 0 - 10.")
            continue
        if table[y][x] == "  " or table[y][x] == "XX":
            print("You've already fire there.Please try again.")
            continue
        else:
            break

def fire():
    global time
    if [y, x] not in ships:
        table[y][x] = "  "
        time = True
    else:
        table[y][x] = "XX"
        time = False
    for ship in ships[0:4]:
        if [y, x] in ships[0:4]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[4:8]:
        if [y, x] in ships[4:8]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[8:11]:
        if [y, x] in ships[8:11]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[11:14]:
        if [y, x] in ships[11:14]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[14:16]:
        if [y, x] in ships[14:16]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[16:18]:
        if [y, x] in ships[16:18]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[18:19]:
        if [y, x] in ships[18:19]:
            table[ship[0]][ship[1]] = "XX"
    for ship in ships[19:20]:
        if [y, x] in ships[19:20]:
            table[ship[0]][ship[1]] = "XX"
    return table

def prnt():
    print("*"*15,"BATTLESHIPS","*"*15)
    print("""\n           WELCOME TO BATTLESHIPS\n
    There are 8 ships.Two of them has 4 unit.
                      Two of them has 3 unit.
                      Two of them has 2 unit.
                      Two of them has 1 unit.
    You can shoot them 15 times.
    You can choose the coordinates to shoot there.""")

table = [["--" for a in range(10)] for b in range(10)]
all_coor = [[a, b] for a in range(10) for b in range(10)]

prnt()
ships = []#all ships which are deployed
turn = 0
deploy()
time = False
try:
    while True:
        if turn == 15:
            print("Game over.You lose.")
            all_ships()
            print_table()
            break
        
        print_table()
        coordinate()
        fire()
        turn += 1

        counter = 0
        for items in table:
            for item in items:
                if item == "XX":
                    counter += 1
        if counter == 20:
            print_table()
            print("\nCongratulations.You've hit the each ships.")
            break
except:
    print("Something happened wrong, please try again")
