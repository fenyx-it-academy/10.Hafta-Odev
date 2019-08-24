import time
game_table = [["    "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","10"],
[" 1  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 2  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 3  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 4  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 5  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 6  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 7  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 8  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 9  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
["10  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],]
game_table1 = [["    "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","10"],
[" 1  ","*4*", "*4*", "*4*","*4*", "___", "___","___", "___", "___","___"],
[" 2  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 3  ","___", "___", "___","___", "___", "___","___", "___", "*1*","___"],
[" 4  ","___", "___", "*4*","___", "___", "___","___", "___", "___","___"],
[" 5  ","*3*", "___", "*4*","___", "*3*", "*3*","*3*", "___", "___","___"],
[" 6  ","*3*", "___", "*4*","___", "___", "___","___", "___", "*1*","___"],
[" 7  ","*3*", "___", "*4*","___", "*2*", "*2*","___", "___", "___","___"],
[" 8  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 9  ","___", "___", "___","___", "___", "___","*2*", "*2*", "___","___"],
["10  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],]
print("\n"*3)
def print_gtable(args):
    for i in args:
        print("\t".expandtabs(30),*i,end="\n"*2)
print_gtable(game_table)
def winning_criteria(args):
    count=0
    for i in args:
        for k in i:
            if k=="*4*" or k=="*3*" or k=="*2*" or k=="*1*":
                count+=1
    return count
number_of_trials=0
count=winning_criteria(game_table1)
while number_of_trials<15:
    count1=winning_criteria(game_table)
    if count==count1:
        print("Congratulations, You win!!!\nYou destroyed all ships")
        print_gtable(game_table)
        break
    try:
        while True:
            x=int(input("Please enter a number from 1 to 10 (from top to bottom): ")
            if x>10 or x<1:
                print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
                continue
            y=int(input("Please enter a number from 1 to 10 (from left to right): ")
            if y>10 or y<1:
                print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
                continue
            break
    except ValueError:
        print("You made an incorrect entry. Please check and read instructions!!!\n")
        continue
    if game_table[x][y]!="___":
        print("\nPlease be careful!!!\nYou have tried to hit this target before.\nPlease check the coordinates of the target!!!")
        number_of_trials += 1
        print("Remaining trial is:", 15 - number_of_trials)
        print_gtable(game_table)
        time.sleep(5)
    elif game_table1[x][y]=="*4*":
        print("\n***Congratulations***, you hit a 4-unit ship!!!\n")
        game_table[x][y]=game_table1[x][y]
        print_gtable(game_table)
    elif game_table1[x][y]=="*3*":
        print("\n***Congratulations***, you hit a 3-unit ship!!!\n")
        game_table[x][y]=game_table1[x][y]
        print_gtable(game_table)
    elif game_table1[x][y]=="*2*":
        print("\n***Congratulations***, you hit a 2-unit ship!!!\n")
        game_table[x][y]=game_table1[x][y]
        print_gtable(game_table)
    elif game_table1[x][y]=="*1*":
        print("\n***Congratulations***, you hit a 1-unit ship!!!\n")
        game_table[x][y]=game_table1[x][y]
        print_gtable(game_table)
    elif game_table[x][y]=="___":
        print("\nSorry, you missed the target!!!")
        game_table[x][y]="X".center(3)
        number_of_trials+=1
        print("Remaining trial is:", 15 - number_of_trials)
        print_gtable(game_table)
        time.sleep(5)
if number_of_trials==15:
    print("You have used 15 trials and You could not destroy all ships!!!\nYOU LOST!!!\nThis is the starting table of the game where all the ships are placed!!!\n")
    print_gtable(game_table1)
