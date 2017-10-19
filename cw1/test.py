#cw1.py
#prepare urself for some long af code

# record play history, i.e. the sequence of moves that the players make during a game,
# so that each game that is played can be recorded and replayed.

# undo and redo, again selecting the most appropriate data structures to enable these functionalities.
# implement an algorithm that enables the computer to choose which moves to make during their own turn,
# i.e. a simple AI player.

# Your choice of algorithm for the AI player may be from the literature, or of your own design. Whichever your
# choice you must be able to evaluate and justify your selection of both data structures and algorithms.
# The game should run from the command line, using a text based interface in the first instance.

# PLS LET ME PASS LOL

##########
# SETUP #
#########

#http://www.darkfish.com/checkers/rules.html (rules)

import sys # used for breaking loops in function

#setup vars
player_1 = "r" #red
player_1K = "R" #Red.
player_2 = "b" #black
player_2K = "B" #BONELESS
move_turn = 1 #var for incrementing turns
current_turn = 1
current_player = ""
enemy_player = ""
player_X = "" #controlling player
player_XK = "" #controlling player (if king piece)
player_Y = "" #other player
player_YK = "" #other player (if king piece)


#create grid
b_grid = [[' ','b',' ','b',' ','b',' ','b'], #[0][0] to [0][7]
          ['b',' ','b',' ','b',' ','b',' '],
          [' ','b',' ','b',' ','b',' ','b'],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          ['r',' ','r',' ','r',' ','r',' '],
          [' ','r',' ','r',' ','r',' ','r'],
          ['r',' ','r',' ','r',' ','r',' ']] #[7][0] to [7][7]


## define functions ##

#print out the rules
def startup_rules():
    print ("Aim to remove all of the opponents pieces!")
    print ("Type 'move' to move a piece")
    print ("Type 'rules' for how to play.")
    print ("Type 'exit' to quit.\n")

#print out how to play
def rules():
    print ("\n* RULES *")
    print ("• You play as Red (r/R), the AI plays as Black(b/B).")
    print ("• Move the pieces diagonally forward to remove the other players pieces.")
    print ("• Type the number of the direction you would like to move.")
    print ("• Moving a piece to the opponents side will make that piece into a King.")
    print ("• King pieces can move back and forth diagonally.\n")

#print board
def print_grid():
    print ("    0   1   2   3   4   5   6   7 ")
    print ("  +-------------------------------+")
    i = 0
    j = 0
    #print same lines 8 times, i and j increment by 1 each loop
    while i < 8:
        print (str(j) + " | "+b_grid[i][0]+" | "+b_grid[i][1]+" | "+b_grid[i][2]+" | "+b_grid[i][3]+" | "+b_grid[i][4]+" | "+b_grid[i][5]+" | "+b_grid[i][6]+" | "+b_grid[i][7]+ " |")
        # to make board look nicer, print different horizontal line
        if i < 7:
            print ("  +---+---+---+---+---+---+---+---+")
        i += 1
        j += 1
    print ("  +-------------------------------+")

# def update_player():
#     global player_1
#     global player_1K
#     global player_2
#     global player_2K
#     global move_turn
#
#     if move_turn % 2 == 0:
#         player_X = (player_2)
#         player_Y = (player_1)
#         current_player == (player_X)
#         enemy_player == (player_Y)
#     else:
#         player_X = (player_1)
#         player_Y = (player_2)
#         current_player = (player_X)
#         enemy_player = (player_Y)

def get_input():
    global split_fromX
    global split_fromY

    print("\nPlease enter the co-ordinates of the piece you would like to move\n('cancel' to exit): ")
    move_from = input("> ") #input co-ord to move from

    while (len(move_from) != 3): #keep looping until string meets requirements
        if (move_from == 'cancel' or move_from == ''): #allow out of loop
            print ("Move cancelled...\n")
            make_move()
        elif (move_from == 'exit'): #if player wants to quit
            print ("Thanks for playing!\n")
            sys.exit()

        #ask user to reinput co-ords
        print ("Please enter in the format x,y: ")
        coord_input = input("> ")
        if (len(coord_input) == 3): #if meets requirements then convert
            move_from = coord_input
        elif (coord_input == 'exit'): #allow user to quit
            print ("Thanks for playing!\n")
            sys.exit()
    else:
        split_from = move_from.split(',') #var to split by comma (creates into array)
        split_fromX = int(split_from[0])
        split_fromY = int(split_from[1])
        print (len(move_from))

def get_dir():
    global current_player
    global move_to

    print ("\nWhere would you like to move your choice?")
    print ("1   2")
    print ("  "+ player_1 +"  ") ###### change to current_player
    print ("3   4\n")
    move_to = input("Please enter your choice ('cancel to exit'): \n")

#when player wants to make a move
def make_move():
    global move_turn # set global
    global split_fromX
    global split_fromY
    global move_to

    get_input()
    get_dir()
    #check if co-ords are in grid
    # if ((split_fromY) >= 0 and (split_fromY) <= 7 or (split_fromX) >= 0 and (split_fromX) <= 7):
    #     if ((b_grid[split_fromY][split_fromX] == player_1)):
            #co-ord to move to


    #if user chooses 1
    if (move_to == '1'):
        #only player 1 piece or AI King can move in direction 1
        if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R' or (b_grid[split_fromY][split_fromX]) == 'B'):
            if ((split_fromY - 1) >= 0 or (split_fromX - 1) >= 0): #check that space is in grid
                if ((b_grid[split_fromY - 1][split_fromX - 1]) == 'b' or (b_grid[split_fromY - 1] [split_fromX - 1]) == 'B'): # check if enemy piece
                    if ((b_grid[split_fromY - 2][split_fromX - 2]) == ' '): #if the space after enemy piece is free

                        #if the y co-ord is last row (0)
                        if ((split_fromY - 2) == 0):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX - 1] = ' '
                            b_grid[split_fromY - 2][split_fromX - 2] = (player_1K)
                            move_turn += 1 #update the turn

                        else:
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX - 1] = ' '
                            b_grid[split_fromY - 2][split_fromX - 2] = (player_1)
                            move_turn += 1 #update the turn
                    else:
                        print ("You cannot move here! (No empty space)\n ")

                #if empty space instead
                elif ((b_grid[split_fromY - 1][split_fromX - 1]) == ' '):
                    #if already king piece
                    if ((b_grid[split_fromY][split_fromX]) == 'R'):
                        b_grid[split_fromY][split_fromX] = ' '
                        b_grid[split_fromY - 1][split_fromX - 1] = (player_1K)
                        move_turn += 1 #update the turn

                    #if normal piece
                    elif ((b_grid[split_fromY][split_fromX]) == 'r'):
                        #if y co-ord in direction is last row
                        if ((split_fromY - 1) == 0):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX - 1] = (player_1K)
                            move_turn += 1 #update the turn
                        else:
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX - 1] = (player_1)
                            move_turn += 1 #update the turn

                    else:
                        print ("This space is not empty!\n")
                else:
                    print ("You cannot move here! (No empty space)\n")
            else:
                print ("This is not in the grid!\n")
        else:
            print ("This piece cannot move in that direction! (Only player 1 or King pieces)\n")

    #if user chooses 2
    elif (move_to == '2'):
        #only player 1 piece or AI King can move in direction 2
        if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R' or (b_grid[split_fromY][split_fromX]) == 'B'):
            if ((split_fromY - 1) >= 0 or (split_fromX + 1) <= 7): #check that space is in grid
                if (b_grid[split_fromY - 1][split_fromX + 1] == 'b'): # check if enemy piece
                    if ((b_grid[split_fromY - 2][split_fromX + 2]) == ' '): #if the space after enemy piece is free

                        #if the y co-ord is last row (0)
                        if ((split_fromY - 2) == 0):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX + 1] = ' '
                            b_grid[split_fromY - 2][split_fromX + 2] = (player_1K)
                            move_turn += 1 #update the turn

                        else:
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX + 1] = ' '
                            b_grid[split_fromY - 2][split_fromX + 2] = (player_1)
                            move_turn += 1 #update the turn
                    else:
                        print ("You cannot move here! (No empty space)\n ")

                #if empty space instead
                elif ((b_grid[split_fromY - 1][split_fromX + 1]) == ' '):
                    #if already king piece
                    if ((b_grid[split_fromY][split_fromX]) == 'R'):
                        b_grid[split_fromY][split_fromX] = ' '
                        b_grid[split_fromY - 1][split_fromX + 1] = (player_1K)
                        move_turn += 1 #update the turn

                    #if normal piece
                    elif ((b_grid[split_fromY][split_fromX]) == 'r'):
                        #if y co-ord in direction is last row
                        if ((split_fromY - 1) == 0):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX + 1] = (player_1K)
                            move_turn += 1 #update the turn
                        else:
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX + 1] = (player_1)
                            move_turn += 1 #update the turn

                    else:
                        print ("This space is not empty!\n")
                else:
                    print ("You cannot move here! (No empty space)\n")
            else:
                print ("This is not in the grid!\n")
        else:
            print ("This piece cannot move in that direction! (Only player 1 or King pieces)\n")


    #if user chooses 3, AI or king only
    elif (move_to == '3'):
        #only AI piece or player 1 King can move in direction 3
        if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B' or (b_grid[split_fromY][split_fromX]) == 'R'):
            if ((split_fromY + 1) <= 7 or (split_fromX - 1) >= 0): #check that space is in grid
                if ((b_grid[split_fromY + 1][split_fromX - 1]) == 'r' or (b_grid [split_fromY + 1][split_fromX - 1]) == 'R'): # check if enemy piece
                    if ((b_grid[split_fromY + 2][split_fromX - 2]) == ' '): #if the space after enemy piece is free

                        #if piece is AI
                        if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B'):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY + 1][split_fromX - 1] = ' '
                            b_grid[split_fromY + 2][split_fromX - 2] = (player_1K)
                            move_turn += 1 #update the turn

                        #if piece is player 1s piece
                        elif ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R'):
                            print ("You cannot move here! (No empty space)\n")
                    else:
                        print ("You cannot move here! (No empty space)\n ")

                elif ((b_grid[split_fromY + 1][split_fromX - 1] == 'b') or (b_grid[split_fromY + 1][split_fromX - 1]) == 'B'): #if player 1 piece
                    if ((b_grid[split_fromY + 2][split_fromX - 2]) == ' '):

                        #if player piece
                        if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R'):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY + 1][split_fromX - 1] = ' '
                            b_grid[split_fromY + 2][split_fromX - 2] = (player_1K)
                            move_turn += 1 #update the turn

                        #if AI piece
                        elif ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B'):
                            print ("You cannot move here! (No empty space)\n")
                    else:
                        print ("You cannot move here! (No empty space)\n")

                #if empty space instead
                elif ((b_grid[split_fromY + 1][split_fromX - 1]) == ' '):
                    b_grid[split_fromY][split_fromX] = ' '
                    b_grid[split_fromY + 1][split_fromX - 1] = (player_1K)
                    move_turn += 1 #update the turn
                else:
                    print ("You cannot move here! (No empty space)\n")
            else:
                print ("This is not in the grid!\n")
        else:
            print ("This piece cannot move in that direction! (Only AI or King pieces)\n")


    #if user chooses 4, king only
    elif (move_to == '4'):
        #only AI piece or player 1 King can move in direction 4
        if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B' or (b_grid[split_fromY][split_fromX]) == 'R'):
            if ((split_fromY + 1) <= 7 or (split_fromX + 1) <= 7): #check that space is in grid
                if ((b_grid[split_fromY + 1][split_fromX + 1]) == 'r' or (b_grid [split_fromY + 1][split_fromX + 1]) == 'R'): # check if enemy piece
                    if ((b_grid[split_fromY + 2][split_fromX + 2]) == ' '): #if the space after enemy piece is free

                        #if piece is AI
                        if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B'):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY + 1][split_fromX + 1] = ' '
                            b_grid[split_fromY + 2][split_fromX + 2] = (player_1K)
                            move_turn += 1 #update the turn

                        #if piece is player 1s piece
                        elif ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R'):
                            print ("You cannot move here! (No empty space)\n")
                    else:
                        print ("You cannot move here! (No empty space)\n ")

                elif ((b_grid[split_fromY + 1][split_fromX + 1] == 'b') or (b_grid[split_fromY + 1][split_fromX + 1]) == 'B'): #if player 1 piece
                    if ((b_grid[split_fromY + 2][split_fromX + 2]) == ' '):
                        print ("ive reached point 5")

                        #if player piece
                        if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R'):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY + 1][split_fromX + 1] = ' '
                            b_grid[split_fromY + 2][split_fromX + 2] = (player_1K)
                            move_turn += 1 #update the turn

                        #if AI piece
                        elif ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B'):
                            print ("You cannot move here! (No empty space)\n")
                    else:
                        print ("You cannot move here! (No empty space)\n")

                #if empty space instead
                elif ((b_grid[split_fromY + 1][split_fromX + 1]) == ' '):
                        b_grid[split_fromY][split_fromX] = ' '
                        b_grid[split_fromY + 1][split_fromX + 1] = (player_1K)
                        move_turn += 1 #update the turn
                else:
                    print ("You cannot move here! (No empty space)\n")
            else:
                print ("This is not in the grid!\n")
        else:
            print ("This piece cannot move in that direction! (Only AI or King pieces)\n")

    elif move_to == 'cancel' or move_to == '':
        print ("\nMove cancelled...\n")
        pass


########
# GAME #
########

print ("** Now playing: Checkers! **\n")
startup_rules()

user_input = input("Please press enter to start: \n")
while (user_input != 'exit'):
    print_grid()

    #to start game, move a piece
    print ("Type move to move a piece")
    user_input = input("> ")

    if user_input == 'rules':
        rules()

    #if user wants to move a piece
    elif user_input == 'move':
        #update_player()
        make_move()
        print ("Turns taken: " + str(move_turn))
        print ("Curent player: " + str(current_player)+ "\n")

    #if user wants to see rules
    elif user_input == 'print':
        print_grid()

    #if user wants to quit
    else:
        break
    #print ("Current Player: ")
    #print ("Current Turn: \n")

#when game ends
print ("\nThanks for playing!\n")
