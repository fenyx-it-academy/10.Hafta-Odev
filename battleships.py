from random import randint,choice

table = [["--" for i in range(10)] for i in range(10)]

all_coor = [[a, b] for a in range(10) for b in range(10)]

#all ships which are deployed
ships = []
#for ships which has 4 units
counter = 0
while True:
    mark = randint(0,1)
    if counter == 2:
        break
    
    elif mark == 0:
        first_coor = choice(all_coor)
        if first_coor[0] > 6:
            first_coor[0] = 6
        second_coor = [first_coor[0] + 1] + [first_coor[1]]
        third_coor = [first_coor[0] + 2] + [first_coor[1]]
        fourth_coor = [first_coor[0] + 3] + [first_coor[1]]
        if first_coor not in ships and second_coor not in ships and third_coor not in ships and fourth_coor not in ships:
            ships.extend([first_coor, second_coor, third_coor, fourth_coor])
            counter += 1
        else:
            continue
        
    elif mark == 1:
        first_coor = choice(all_coor)
        if first_coor[1] > 6:
            first_coor[1] = 6
        second_coor = [first_coor[0]] + [first_coor[1] + 1]
        third_coor = [first_coor[0]] + [first_coor[1] + 2]
        fourth_coor = [first_coor[0]] + [first_coor[1] + 3]
        if first_coor not in ships and second_coor not in ships and third_coor not in ships and fourth_coor not in ships:
            ships.extend([first_coor, second_coor, third_coor, fourth_coor])
            counter += 1
        else:
            continue
#for ships which has 3 units
counter = 0
while True:
    mark = randint(0,1)
    if counter == 2:
        break
    
    elif mark == 0:
        first_coor = choice(all_coor)
        if first_coor[0] > 7:
            first_coor[0] = 7
        second_coor = [first_coor[0] + 1] + [first_coor[1]]
        third_coor = [first_coor[0] + 2] + [first_coor[1]]
        if first_coor not in ships and second_coor not in ships and third_coor not in ships:
            ships.extend([first_coor, second_coor, third_coor])
            counter += 1
        else:
            continue
        
    elif mark == 1:
        first_coor = choice(all_coor)
        if first_coor[1] > 7:
            first_coor[1] = 7
        second_coor = [first_coor[0]] + [first_coor[1] + 1]
        third_coor = [first_coor[0]] + [first_coor[1] + 2]
        if first_coor not in ships and second_coor not in ships and third_coor not in ships:
            ships.extend([first_coor, second_coor, third_coor])
            counter += 1
        else:
            continue
#for ships which has 2 units
counter = 0
while True:
    mark = randint(0,1)
    if counter == 2:
        break
    
    elif mark == 0:
        first_coor = choice(all_coor)
        if first_coor[0] > 8:
            first_coor[0] = 8
        second_coor = [first_coor[0] + 1] + [first_coor[1]]
        if (first_coor not in ships) and (second_coor not in ships):
            ships.extend([first_coor, second_coor])
            counter += 1
        else:
            continue
        
    elif mark == 1:
        first_coor = choice(all_coor)
        if first_coor[1] > 8:
            first_coor[1] = 8
        second_coor = [first_coor[0]] + [first_coor[1] + 1]
        if (first_coor not in ships) and (second_coor not in ships):
            ships.extend([first_coor, second_coor])
            counter += 1
        else:
            continue
#for ships which has 1 unit
counter = 0
while True:
    mark = randint(0,1)
    if counter == 2:
        break
    coor = choice(all_coor)
    if coor not in ships:
            ships.extend([coor])
            counter += 1
    else:
        continue
    
        
def all_ships():
    for ship in ships:
        table[ship[0]][ship[1]] = "XX"
    return table

def print_table():
    for item in table:
        print("\n\t".expandtabs(20),*item)
def coordinate():
    global y
    global x
    y = int(input("\nPlease choose the y axis:"))
    x = int(input("\nPlease choose the x axis:"))
    y = y - 1
    x = x - 1

def fire():
    if [y, x] not in ships:
        table[y][x] = "  "
    else:
        table[y][x] = "XX"
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
    

print("*"*15,"BATTLESHIPS","*"*15)
print("""\n           WELCOME TO BATTLESHIPS\n
There are 8 ships.Two of them has 4 unit.
                  Two of them has 3 unit.
                  Two of them has 2 unit.
                  Two of them has 1 unit.
You can shoot them 15 times.
You can choose the coordinates to shoot there.""")
turn = 0
try:
    while True:
        print_table()
        coordinate()
        fire()
        turn += 1

        if turn == 16:
            print("Game over.You lose.")
            all_ships()
            print_table()
            break
        
        counter = 0
        for items in table:
            for item in items:
                if item == "XX":
                    counter += 1
        if counter == 20:
            print_table()
            print("\nCongratulations.You've hit the each ships.")
            break
except ValueError:
    print("Please try again and enter a number")
except IndexError:
    print("Please try again and enter a number between 1 and 10")    
except:
    print("Something happened wrong, please try again")
            
    



    
            

  

    





