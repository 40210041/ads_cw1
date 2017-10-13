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

#setup vars
player_1 = "r" #red
player_1K = "R" #Red.
player_2 = "b" #black
player_2K = "B" #BONELESS
move_turn = 0 #var for incrementing turns
current_turn = 0
current_player = ""

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
        #co-ord to move from
        print("\nPlease enter the co-ordinates of the piece you would like to move\n('cancel' to exit): ")
        move_from = input("> ") #input co-ord to move from
        if move_from == 'cancel' or move_from == '': #allow out of loop
            print ("\nMove cancelled...\n")
            pass #null

        else:
            split_from = move_from.split(',') #var to split by comma (creates into array)
            split_fromX = int(split_from[0])
            split_fromY = int(split_from[1])

            #check if co-ords are in grid
            # if ((split_fromY) >= 0 and (split_fromY) <= 7 or (split_fromX) >= 0 and (split_fromX) <= 7):
            #     if ((b_grid[split_fromY][split_fromX] == player_1)):
                    #co-ord to move to
            print ("\nWhere would you like to move your choice?")
            print ("1   2")
            print ("  "+ player_1 +"  ") ###### change to current_player
            print ("3   4\n")
            move_to = input("Please enter your choice ('cancel to exit'): \n")

            #if user chooses 1
            if (move_to == '1'):
                #only player 1 piece or AI King can move in direction 1
                if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R' or (b_grid[split_fromY][split_fromX]) == 'B'):
                    if ((split_fromY - 1) >= 0 or (split_fromX - 1) >= 0): #check that space is in grid
                        if (b_grid[split_fromY - 1][split_fromX - 1] == 'b'): # check if enemy piece
                            if ((b_grid[split_fromY - 2][split_fromX - 2]) == ' '): #if the space after enemy piece is free
                                print ("ive reached point 1!")
                                print ("There's an enemy piece here! You must take it!\n")

                                #if the y co-ord is last row (0)
                                if ((split_fromY - 2) == 0):
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX - 1] = ' '
                                    b_grid[split_fromY - 2][split_fromX - 2] = (player_1K)

                                else:
                                    print ("ive reached point 2!")
                                    b_grid[split_fromY][split_fromX] = ' '
                                    b_grid[split_fromY - 1][split_fromX - 1] = ' '
                                    b_grid[split_fromY - 2][split_fromX - 2] = (player_1)
                            else:
                                print ("You cannot move here! (No empty space)\n ")

                        #if empty space instead
                        elif ((b_grid[split_fromY - 1][split_fromX - 1]) == ' '):
                            print ("ive reached point 3!")
                            #if y co-ord in direction
                            if ((split_fromY - 1) == 0):
                                b_grid[split_fromY][split_fromX] = ' '
                                b_grid[split_fromY - 1][split_fromX - 1] = (player_1K)

                            #if already king piece
                            elif ((b_grid[split_fromY][split_fromX]) == 'R'):
                                b_grid[split_fromY][split_fromX] = ' '
                                b_grid[split_fromY - 1][split_fromX - 1] = (player_1)

                            elif ((b_grid[split_fromY][split_fromX]) == 'r'):
                                b_grid[split_fromY][split_fromX] = ' '
                                b_grid[split_fromY - 1][split_fromX - 1] = player_1

                            else:
                                print ("This space is not empty!\n")
                        else:
                            print ("You cannot move here!\n")
                    else:
                        print ("Not in the grid!\n")
                else:
                    print ("This piece cannot move in that direction!\n")

            #if user chooses 2
            elif (move_to == '2'):
                if (b_grid[split_fromY][split_fromX]) == 'R':
                    if (b_grid[split_fromY - 1][split_fromX + 1]) == " ":
                        b_grid[split_fromY][split_fromX] = " "
                        b_grid[split_fromY - 1][split_fromX + 1] = (player_1)
                    else:
                        print ("This space is not empty\n")
                elif (b_grid[split_fromY][split_fromX]) == 'r':
                    if (b_grid[split_fromY - 1][split_fromX + 1]) == " ":
                        b_grid[split_fromY][split_fromX] = " "
                        b_grid[split_fromY - 1][split_fromX + 1] = (player_1)
                else:
                    print ("This space is not empty\n")

            #if user chooses 3, king only
            elif (move_to == '3'):
                if (b_grid[split_fromY][split_fromX]) == 'R':
                    if (b_grid[split_fromY + 1][split_fromX - 1]) == " ":
                        b_grid[split_fromY][split_fromX] = " "
                        b_grid[split_fromY + 1][split_fromX - 1] = (player_1K)
                    else:
                        print ("This space is not empty\n")
                else:
                    print ("\nOnly King pieces can move backwards!\n")

            #if user chooses 4, king only
            elif (move_to == '4'):
                if (b_grid[split_fromY][split_fromX]) == 'R':
                    if (b_grid[split_fromY + 1][split_fromX + 1]) == " ":
                        b_grid[split_fromY][split_fromX] = " "
                        b_grid[split_fromY + 1][split_fromX + 1] = "R"
                    else:
                        print ("This space is not empty\n")
                else:
                    print ("\nOnly King pieces can move backwards!\n")

            elif move_to == 'cancel' or move_to == '':
                print ("\nMove cancelled...\n")
                pass
        # 		else:
        # 			print ("You do not have a piece here!\n")
    	# else:
    	# 	print ("This co-ordinate is out the grid!\n")

    #if user wants to see rules
    elif user_input == 'rules':
        rules()

    #if user wants to quit
    else:
        break
    #print ("Current Player: ")
    #print ("Current Turn: \n")

#when game ends
print ("\nThanks for playing!\n")
