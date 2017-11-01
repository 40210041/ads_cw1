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

import sys

#http://www.darkfish.com/checkers/rules.html (rules)

#setup vars
player_1 = "r" #red
player_1K = "R" #Red.
player_2 = "b" #black
player_2K = "B" #BONELESS
move_turn = 1 #var for incrementing turns
current_turn = 1
current_player = (player_1)
enemy_player = (player_2)
player_XK = "" #controlling player (if king piece)
player_YK = "" #other player (if king piece)
must_take1 = False
must_take2 = False
must_take3 = False
must_take4 = False

#create grid
b_grid = [[' ','b',' ','b',' ','b',' ','b'], #[0][0] to [0][7]
          ['b',' ','b',' ','b',' ','b',' '],
          [' ','b',' ','b',' ','b',' ','b'],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ','b',' ',' ',' ',' ',' ',' '],
          ['r',' ','r',' ','r',' ','r',' '],
          [' ','r',' ','r',' ','r',' ','r'],
          ['r',' ','r',' ','r',' ','r',' ']] #[7][0] to [7][7]


## define functions ##

#print out the rules
def startup_rules():
    print ("Aim to remove all of the opponents pieces!")
    print ("Type 'move' to move a piece")
    print ("Type 'rules' for how to play.")
    print ("Type 'check' to look at the board.")
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

#check for pieces that must be taken
def mandatory_take():
    global must_take1
    global must_take2
    global must_take3
    global must_take4
    global move_turn

    must_take1 = False
    must_take2 = False
    must_take3 = False
    must_take4 = False

    temp_X = 0 #temp x coord
    temp_Y = 0 #temp y coord

    for i in b_grid: #for each row in the grid
        for j in i: #for each element in i

            #for must_take1
            if (temp_Y >= 2 and temp_X >= 2): #starting point must be able to stay inthe grid after moving 2 spaces around
                if (current_player == (player_1) or current_player == (player_1K) or current_player == (player_2K)): # only player 1 or ai can move this direction
                    if ((b_grid[temp_Y][temp_X] == (player_1)) or (b_grid[temp_Y][temp_X] == (player_1K))): #if the current space is not blank or ai piece
                        if ((b_grid[temp_Y - 1][temp_X - 1] == 'b') or (b_grid[temp_Y - 1][temp_X - 1] == 'B') and (current_player == (player_1) or (player_1K))):
                            if (b_grid[temp_Y - 2][temp_X - 2] == ' '):
                                must_take1 = True
                                print ("The coords 1r: ", str(temp_Y) , str(temp_X))

                    elif ((b_grid[temp_Y][temp_X]) == (player_2) or (b_grid[temp_Y][temp_X]) == (player_2K)):
                        if((b_grid[temp_Y - 1][temp_X - 1]) == 'r' or (b_grid[temp_Y - 1][temp_X - 1]) == 'R' and current_player == (player_2K)):
                            if (b_grid[temp_Y - 2][temp_X - 2] == ' '):
                                must_take1 = True
                                print ("The coords 1b: ", str(temp_Y) , str(temp_X))

            #for must_take2
            if (temp_Y >= 2 and temp_X <= 5): #must stay within grid after moving
                if ((current_player) == (player_1) or (current_player) == (player_1K) or (current_player) == (player_2K)):
                    if ((b_grid[temp_Y][temp_X]) == (player_1) or (b_grid[temp_Y][temp_X]) == (player_1K)):
                        if ((b_grid[temp_Y - 1][temp_X + 1]) == 'b' or (b_grid[temp_Y - 1][temp_X + 1]) == 'B' and (current_player == (player_1) or (player_1K))):
                            if (b_grid[temp_Y - 2][temp_X + 2] == ' '):
                                must_take2 = True
                                print ("The coords 2r: ", str(temp_Y) , str(temp_X))

                    elif ((b_grid[temp_Y][temp_X]) == (player_2) or (b_grid[temp_Y][temp_X]) == (player_2K)):
                        if ((b_grid[temp_Y - 1][temp_X + 1]) == 'r' or (b_grid[temp_Y - 1][temp_X + 1]) == 'B' and current_player == (player_2K)):
                            if ((b_grid[temp_Y - 2][temp_X + 2]) == ' '):
                                must_take2 = True
                                print ("The coords 2b: ", str(temp_Y) , str(temp_X))

            #for must_take3
            if (temp_Y <= 5 and temp_X >= 2): #must stay in grid after moving
                if (current_player == (player_2) or (current_player) == (player_2K) or (current_player) == (player_1K)):
                    if ((b_grid[temp_Y][temp_X]) == (player_2) or (b_grid[temp_Y][temp_X]) == (player_2K)):
                        print ("current space is b", str(temp_Y), str(temp_X))
                        if ((b_grid[temp_Y + 1][temp_X - 1]) == 'r' or (b_grid[temp_Y + 1][temp_X - 1]) == 'R' and ((current_player) == (player_2) or (current_player) == (player_2K))):
                            if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                                must_take3 = True
                                print ("The coords 3b: ", str(temp_Y) , str(temp_X))

                    else:
                        if ((b_grid[temp_Y][temp_X]) == (player_1) or (b_grid[temp_Y][temp_X]) == (player_1K)):
                            print ("current space is r", str(temp_Y), str(temp_X))
                            if ((b_grid[temp_Y + 1][temp_X - 1] == 'b' or 'B') and (current_player) == (player_1K)):
                                if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                                    must_take3 = True
                                    print ("The coords 3r: ", str(temp_Y) , str(temp_X))

            #for must_take4
            if (temp_Y <= 5 and temp_X <= 5): #must stay in grid after moving
                if (current_player == (player_2) or (current_player) == (player_2K) or (current_player) == (player_1K)):
                    if ((b_grid[temp_Y][temp_X]) == (player_2) or (b_grid[temp_Y][temp_X]) == (player_2K)):
                        if ((b_grid[temp_Y + 1][temp_X + 1] == 'r' or 'R') and (current_player == (player_2) or (current_player) == (player_2K))):
                            if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                                must_take4 = True
                                print ("The coords 4b: ", str(temp_Y) , str(temp_X))

                    elif ((b_grid[temp_Y][temp_X]) == (player_1) or (b_grid[temp_Y][temp_X]) == (player_1K)):
                        if ((b_grid[temp_Y + 1][temp_X + 1] == 'b' or 'B') and (current_player) == (player_1K)):
                            if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                                must_take4 = True
                                print ("The coords 4r: ", str(temp_Y) , str(temp_X))

            if (must_take1 == True or must_take2 == True or must_take3 == True or must_take4 == True): #if one of the statements are true
                print ("You must choose to move one of the following pieces: ")
                must_take = []

                #print out options that can be taken
                if (must_take1 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 1")
                    must_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take2 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 2")
                    must_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take3 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 3")
                    must_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take4 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 4")
                    must_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                ####### REMOVE #########
                print (must_take)
                print (must_take1)
                print (must_take2)
                print (must_take3)
                print (must_take4)

                print ("Please enter your choice: ")
                user_take = input("> ")
                #if the user move and must == true then make move ie starndard move preocedure jhahahahaha

                if (must_take1 == True and user_take == "1"):
                    b_grid[temp_Y][temp_X] == (' ')
                    b_grid[temp_Y - 1][temp_X - 1] == (' ')
                    b_grid[temp_Y - 2][temp_X - 2] == (current_player)
                    move_turn += 1
                    print (temp_X)
                    print (temp_Y)

                elif (must_take2 == True and user_take == "2"):
                    b_grid[temp_Y][temp_X] == (' ')
                    b_grid[temp_Y - 1][temp_X + 1] == (' ')
                    b_grid[temp_Y - 2][temp_X + 2] == (current_player)
                    move_turn += 1
                    print (temp_X)
                    print (temp_Y)

                elif (must_take3 == True and user_take == '3'):
                    b_grid[temp_Y][temp_X] == ' '
                    b_grid[temp_Y + 1][temp_X - 1] == ' '
                    b_grid[temp_Y + 2][temp_X - 2] == (current_player)
                    move_turn += 1
                    print (temp_X)
                    print (temp_Y)

                elif (must_take4 == True and user_take == '4'):
                    b_grid[temp_Y][temp_X] == ' '
                    b_grid[temp_Y + 1][temp_X + 1] == ' '
                    b_grid[temp_Y + 2][temp_X + 2] == (current_player)
                    move_turn += 1
                    print (temp_X)
                    print (temp_Y)

                else:
                    print ("You did not choose an option...\n")
                    pass

            #reset variables to be false
            must_take1 = False
            must_take2 = False
            must_take3 = False
            must_take4 = False

            #for each element in i, increase till 7 then start on next line
            temp_X +=1
            if (temp_X > 7):
                temp_X = 0
        #increase the current row (i)
        temp_Y += 1
    print_grid()

#get coord for moving a piece
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
            print ("\nThanks for playing!\n")
            sys.exit()

        #ask user to reinput co-ords
        print ("\nPlease enter in the format 'x,y': ")
        coord_input = input("> ")
        if (len(coord_input) == 3 and coord_input[0].isnumeric() and coord_input[2].isnumeric() and coord_input[1] == ','): #if meets requirements then convert
            move_from = coord_input

        elif (coord_input == 'exit'): #allow user to quit
            print ("\nThanks for playing!\n")
            sys.exit()
    else:
        if (len(move_from) == 3 and move_from[0].isnumeric() and move_from[2].isnumeric() and move_from[1] == ','):
            split_from = move_from.split(',') #var to split by comma (creates into array)
            split_fromX = int(split_from[0])
            split_fromY = int(split_from[1])
        else:
            get_input() #if conditions not met out of loop, go back to beginning

#get direction to move piece
def get_dir():
    global current_player
    global move_to

    print ("\nWhere would you like to move your choice?")
    print ("1   2")
    print ("  "+ current_player +"  ") ###### change to current_player
    print ("3   4\n")
    move_to = input("Please enter your choice ('cancel to exit'): \n")

#maake a move
def make_move():
    global move_turn # set global
    global split_fromX
    global split_fromY
    global move_to

    get_input()
    #check if coords are in grid
    if ((split_fromY) >= 0 and (split_fromY) <= 7 or (split_fromX) >= 0 and (split_fromX) <= 7):
        #check if oiece belongs to current player
        if ((b_grid[split_fromY][split_fromX] == current_player)):

            #if meets requirements are met then get directon
            get_dir()

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

                        #if piece is ai piece and current player is ai
                        elif ((b_grid[split_fromY][split_fromX]) == 'B' and current_player == (player_2)):
                            print ("This is an enemy king!")
                            if ((b_grid[split_fromY - 1][split_fromX - 1]) == 'b' or  (b_grid[split_fromY][split_fromX]) == 'B'):
                                print ("You cannot move here! (No free space)\n")

                            elif ((b_grid[split_fromY - 1][split_fromX - 1]) == 'r' or (b_grid[split_fromY - 1][split_fromX - 1]) == 'R'):
                                if ((b_grid[split_fromY - 2][split_fromX - 2]) == ' '):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX - 1] = ' '
                                    b_grid[split_fromY - 2][split_fromX - 2] = (player_2K)

                            elif ((b_grid[split_fromY - 1][split_fromX - 1]) == ' '):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX - 1] = (player_2K)

                            else:
                                print ("You do not have a piece here!\n")

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

                        #if piece is ai piece and current player is ai
                        elif ((b_grid[split_fromY][split_fromX]) == 'B' and current_player == (player_2)):
                            print ("This is an enemy king!")
                            if ((b_grid[split_fromY - 1][split_fromX + 1]) == 'b' or  (b_grid[split_fromY][split_fromX]) == 'B'):
                                print ("You cannot move here! (No free space)\n")

                            elif ((b_grid[split_fromY - 1][split_fromX + 1]) == 'r' or (b_grid[split_fromY - 1][split_fromX - 1]) == 'R'):
                                if ((b_grid[split_fromY - 2][split_fromX + 2]) == ' '):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX + 1] = ' '
                                    b_grid[split_fromY - 2][split_fromX + 2] = (player_2K)

                            elif ((b_grid[split_fromY - 1][split_fromX + 1]) == ' '):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX + 1] = (player_2K)

                            else:
                                print ("You do not have a piece here!\n")


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
                                if ((b_grid[split_fromY][split_fromX]) == 'b'):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY + 1][split_fromX - 1] = ' '
                                    b_grid[split_fromY + 2][split_fromX - 2] = (player_2K)
                                    move_turn += 1

                                elif ((b_grid[split_fromY][split_fromX]) == 'B'):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY + 1][split_fromX - 1] = ' '
                                    b_grid[split_fromY + 2][split_fromX - 2] = (player_2K)
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
                            b_grid[split_fromY + 1][split_fromX - 1] = (current_player)
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
                                    b_grid[split_fromY + 2][split_fromX + 2] = (player_2K)
                                    move_turn += 1 #update the turn

                                #if piece is player 1s piece
                                elif ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R'):
                                    print ("You cannot move here! (No empty space)\n")
                            else:
                                print ("You cannot move here! (No empty space)\n ")

                        elif ((b_grid[split_fromY + 1][split_fromX + 1] == 'b') or (b_grid[split_fromY + 1][split_fromX + 1]) == 'B'): #if player 1 piece
                            if ((b_grid[split_fromY + 2][split_fromX + 2]) == ' '):
                                print ("ive reached point 5")
                                print ("There is an enemy piece here! You must take it!\n")

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
                                b_grid[split_fromY + 1][split_fromX + 1] = (current_player)
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

        else:
            print ("You do not have a piece here!\n")
    else:
        print ("This is not in the grid!\n")

#update player
def update_player():
    global player_1
    global player_1K
    global player_2
    global player_2K
    global current_player
    global enemy_player
    global move_turn

    if move_turn % 2 == 0:
        # player_X = (player_2)
        # player_Y = (player_1)
        current_player = (player_2)
        enemy_player = (player_1)
    else:
        # player_X = (player_1)
        # player_Y = (player_2)
        current_player = (player_1)
        enemy_player = (player_2)

########
# GAME #
########

print ("\n** Now playing: Checkers! **\n")
startup_rules()

user_input = input("Please press enter to start: \n")
while (user_input != 'exit'):
    print_grid()
    print ("\n\nCurrent turn: " + str(move_turn))
    print ("Current player: " + str(current_player)+ "\n")

    #to start game, move a piece
    print ("Type move to move a piece")
    user_input = input("> ")

    if user_input == 'rules':
        rules()

    #if user wants to move a piece
    elif user_input == 'move':
        mandatory_take()
        make_move()
        update_player()


    #if user wants to see rules
    elif user_input == 'check':
        print_grid()

    #if user wants to quit
    else:
        break

#when game ends
print ("\nThanks for playing!\n")
