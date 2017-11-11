#cw1.py

##########
# SETUP #
#########
import copy
import sys
import random

#http://www.darkfish.com/checkers/rules.html (rules)

#setup vars
against_ai = False
player_1 = "r" #red
player_1K = "R" #red king
player_2 = "b" #black
player_2K = "B" #black king
move_turn = 1 #var for incrementing turns
current_player = (player_1) #current player piece
current_king = (player_1K) #current player king
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

undo_grid = b_grid[:]
redo_grid = b_grid[:]


## define functions ##

#print out the rules
def startup_rules():
    print ("Aim to remove all of the opponents pieces!")
    print ("Type 'move' to move a piece")
    print ("Type 'rules' for how to play (* NOTE * Please read the rules before playing!).")
    print ("Type 'check' to look at the board.")
    print ("Type 'exit' to quit.\n")

#print out how to play
def rules():
    print ("\n* RULES *")
    print ("• P1 plays as Red (r/R), the AI/P2 plays as Black(b/B).")
    print ("• Move the pieces forward to remove the other players pieces.")
    print ("• Type the co-ordinates of the piece that you would like to move.")
    print ("• Type the number of the direction you would like to move.")
    print ("• Moving a piece to the end of the opponents side will make that piece into a King.")
    print ("• King pieces can move back and forth diagonally.\n")
    print ("* HOW TO PLAY *")
    print ("• Type 'move' to move a piece.")
    print ("• Type 'check' to look at the current player and board.")
    print ("• Type 'undo' to undo the previous move (one move only per turn).")
    print ("• Type 'redo' to redo the current move if undone (only if the previous move has been undone).")
    print ("• * NOTE * You cannot undo during a move, only before or after!")
    print ("• * NOTE * You cannot redo the AI's move!")
    print ("• Type 'exit' to quit the game.\n")

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

#determine whether against ai or another player
def ai_p2():
    global against_ai, against_p2

    against_ai = False
    against_p2 = False

    print ("Who would you like to play against?")
    print ("Type '1' to play against an AI.\nType '2' to play against another person.")
    print ("Type 'exit' to quit.")
    print ("Please enter your choice: ")
    game_mode = input("> ")

    if (game_mode == "1"):
        against_ai = True
        against_p2 = False
        print ("\n** You are now playing against an AI, good luck! **\n")

    elif (game_mode == "2"):
        against_ai = False
        against_p2 = True
        print ("\n** You are now playing against another player, good luck! **\n")

    elif (game_mode == 'exit'):
        print ("\n** Thanks for playing! **\n")
        sys.exit()

    else:
        print ("\n* Please choose a valid option! *\n")
        ai_p2()

#update player
def update_player():
    global player_1, player_1K, player_2, player_2K, current_player, current_king, move_turn

    #if move modulo 2 is 0 then player 2's turn
    if (move_turn % 2 == 0):
        current_player = (player_2)
        current_king = (player_2K)
    else:
        current_player = (player_1)
        current_king = (player_1K)

#check for pieces that must be taken
def mandatory_take():
    global current_player, player_1, player_1k, player_2, player_2K
    global must_take1, must_take2, must_take3, must_take4, move_turn, piece_moved

    must_take = False
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
                if (current_player == (player_1) or current_king == (player_2K)): # only player 1 or ai can move this direction
                    if (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)): #if the current space is not blank or ai piece
                        #if the next space is enemy piece
                        if ((b_grid[temp_Y - 1][temp_X - 1] == 'b' or b_grid[temp_Y - 1][temp_X - 1] == 'B') and (current_player == (player_1))):
                            if (b_grid[temp_Y - 2][temp_X - 2] == ' '): # if the space after is empty
                                must_take1 = True
                    elif (b_grid[temp_Y][temp_X] == (player_2K)):
                        if((b_grid[temp_Y - 1][temp_X - 1] == 'r' or b_grid[temp_Y - 1][temp_X - 1] == 'R') and (current_king == (player_2K))):
                            if (b_grid[temp_Y - 2][temp_X - 2] == ' '):
                                must_take1 = True

            #for must_take2
            if (temp_Y >= 2 and temp_X <= 5): #must stay within grid after moving
                if (current_player == (player_1) or current_king == (player_2K)):
                    if (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)):
                        if ((b_grid[temp_Y - 1][temp_X + 1] == 'b' or b_grid[temp_Y - 1][temp_X + 1] == 'B') and (current_player == (player_1))):
                            if (b_grid[temp_Y - 2][temp_X + 2] == ' '):
                                must_take2 = True

                    elif (b_grid[temp_Y][temp_X] == (player_2K)):
                        if ((b_grid[temp_Y - 1][temp_X + 1] == 'r' or b_grid[temp_Y - 1][temp_X + 1] == 'B') and (current_king == (player_2K))):
                            if ((b_grid[temp_Y - 2][temp_X + 2]) == ' '):
                                must_take2 = True

            #for must_take3
            if (temp_Y <= 5 and temp_X >= 2): #must stay in grid after moving
                if (current_player == (player_2) or current_king == (player_1K)):
                    if (b_grid[temp_Y][temp_X] == (player_2) or b_grid[temp_Y][temp_X] == (player_2K)):
                        if ((b_grid[temp_Y + 1][temp_X - 1] == 'r' or b_grid[temp_Y + 1][temp_X - 1] == 'R') and (current_player == (player_2))):
                            if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                                must_take3 = True

                    else:
                        if ((b_grid[temp_Y][temp_X]) == (player_1K)):
                            if ((b_grid[temp_Y + 1][temp_X - 1] == 'b' or b_grid[temp_Y + 1][temp_X - 1]  ==  'B') and (current_king == (player_1K))):
                                if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                                    must_take3 = True

            #for must_take4
            if (temp_Y <= 5 and temp_X <= 5): #must stay in grid after moving
                if (current_player == (player_2) or current_king == (player_1K)):
                    if (b_grid[temp_Y][temp_X] == (player_2) or b_grid[temp_Y][temp_X] == (player_2K)):
                        if ((b_grid[temp_Y + 1][temp_X + 1] == 'r' or b_grid[temp_Y + 1][temp_X + 1] == 'R') and (current_player == (player_2))):
                            if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                                must_take4 = True

                    elif (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)):
                        if ((b_grid[temp_Y + 1][temp_X + 1] == 'b' or b_grid[temp_Y + 1][temp_X + 1] == 'B') and (current_king == (player_1K))):
                            if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                                must_take4 = True


            if (must_take1 == True or must_take2 == True or must_take3 == True or must_take4 == True): #if one of the statements are true
                must_take = True #set to true, if user does not pick a choice then loop back
                print ("\n* There are pieces which must be taken! *\n")
                print ("Press enter to view another choice (if more than one).")
                print ("You must choose to move one of the following pieces: \n")
                ai_take = []

                #print out options that can be taken
                if (must_take1 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 1")
                    ai_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take2 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 2")
                    ai_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take3 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 3")
                    ai_take.append(''+str(temp_X)+','+str(temp_Y)+'')

                if (must_take4 == True):
                    print ("For "+ str(temp_X) +"," + str(temp_Y), "you can choose: 4")
                    ai_take.append(''+str(temp_X)+','+str(temp_Y)+'')


                if (against_ai == True): #if playing against ai
                    # ask user to choose an option depending on results
                    print ("Please enter your choice: ")

                    if (current_player == player_2):
                        if (must_take1 == True):
                            user_take = "1"
                            print ("\nPlayer 2 chose: 1\n")
                        elif (must_take2 == True):
                            user_take= "2"
                            print ("\nPlayer 2 chose: 2\n")
                        elif (must_take3 == True):
                            user_take = "3"
                            print ("\nPlayer 2 chose: 3\n")
                        elif (must_take4 == True):
                            user_take = "4"
                            print ("\nPlayer 2 chose: 4\n")

                    else:
                        user_take = input("> ")

                    if (user_take == "1" or user_take == "2" or user_take == "3" or user_take == "4" or user_take == "exit"):

                        #if the users choice matches with a statement which is true:
                        if (must_take1 == True and user_take == "1"):
                            if (temp_Y - 2 == 0):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X - 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take2 == True and user_take == "2"):
                            if (temp_Y - 2 == 0):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X + 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take3 == True and user_take == '3'):
                            if (temp_Y + 2 == 7):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X - 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take4 == True and user_take == '4'):
                            if (temp_Y + 2 == 7):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X + 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (user_take == "exit"):
                            print ("\n** Thanks for playing! **\n")
                            sys.exit()

                        #if the user does not choose and option
                        else:
                            print ("Please enter a choice or cycle through the choices (if more than one).\n")
                    else:
                        print ("\nPlease enter '1','2','3' or '4'. Or press enter to cycle through the choices (if more than one).\n")

                else:

                    print ("Please enter your choice: ")
                    user_take = input("> ")
                    if (user_take == "1" or user_take == "2" or user_take == "3" or user_take == "4" or user_take == "exit" ):

                        #if the users choice matches with a statement which is true:
                        if (must_take1 == True and user_take == "1"):
                            if (temp_Y - 2 == 0):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X - 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take2 == True and user_take == "2"):
                            if (temp_Y - 2 == 0):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X + 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y - 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y - 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y - 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take3 == True and user_take == '3'):
                            if (temp_Y + 2 == 7):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X - 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X - 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X - 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (must_take4 == True and user_take == '4'):
                            if (temp_Y + 2 == 7):
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X + 2] = (current_king)
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return
                            else:
                                undo_grid = b_grid[:]
                                undo_grid = copy.deepcopy(b_grid)
                                b_grid[temp_Y + 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                                b_grid[temp_Y][temp_X] = (' ')
                                b_grid[temp_Y + 1][temp_X + 1] = (' ')
                                additional_takes(temp_Y + 2, temp_X + 2)
                                move_turn += 1
                                update_player()
                                piece_moved = True
                                return

                        elif (user_take == "exit"):
                            print ("\n** Thanks for playing! **\n")
                            sys.exit()

                        #if the user does not choose and option
                        else:
                            print ("Please enter a choice or cycle through the choices (if more than one).\n")
                    else:
                        print ("\nPlease enter '1','2','3' or '4'. Or press enter to cycle through the choices (if more than one).\n")

            if (temp_Y == 7 and temp_X == 7):
                if (must_take == True):
                    print ("\n* End of list, please make a choice *\n")
                    mandatory_take()

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

#check for any additional takes after the original take
def additional_takes(temp_Y, temp_X):

    #set vars to false
    must_take = False
    must_take1 = False
    must_take2 = False
    must_take3 = False
    must_take4 = False

    #for must_take1
    if (temp_Y >= 2 and temp_X >= 2): #starting point must be able to stay inthe grid after moving 2 spaces around
        if (current_player == (player_1) or current_king == (player_2K)): # only player 1 or ai can move this direction
            if (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)): #if the current space is not blank or ai piece
                if ((b_grid[temp_Y - 1][temp_X - 1] == 'b' or b_grid[temp_Y - 1][temp_X - 1] == 'B') and (current_player == (player_1))):
                    if (b_grid[temp_Y - 2][temp_X - 2] == ' '): # if the space after is empty
                        must_take1 = True
            elif (b_grid[temp_Y][temp_X] == (player_2K)):
                if((b_grid[temp_Y - 1][temp_X - 1] == 'r' or b_grid[temp_Y - 1][temp_X - 1] == 'R') and (current_king == (player_2K))):
                    if (b_grid[temp_Y - 2][temp_X - 2] == ' '):
                        must_take1 = True

    #for must_take2
    if (temp_Y >= 2 and temp_X <= 5): #must stay within grid after moving
        if (current_player == (player_1) or current_king == (player_2K)):
            if (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)):
                if ((b_grid[temp_Y - 1][temp_X + 1] == 'b' or b_grid[temp_Y - 1][temp_X + 1] == 'B') and (current_player == (player_1))):
                    if (b_grid[temp_Y - 2][temp_X + 2] == ' '):
                        must_take2 = True

            elif (b_grid[temp_Y][temp_X] == (player_2K)):
                if ((b_grid[temp_Y - 1][temp_X + 1] == 'r' or b_grid[temp_Y - 1][temp_X + 1] == 'B') and (current_king == (player_2K))):
                    if ((b_grid[temp_Y - 2][temp_X + 2]) == ' '):
                        must_take2 = True

    #for must_take3
    if (temp_Y <= 5 and temp_X >= 2): #must stay in grid after moving
        if (current_player == (player_2) or current_king == (player_1K)):
            if (b_grid[temp_Y][temp_X] == (player_2) or b_grid[temp_Y][temp_X] == (player_2K)):
                if ((b_grid[temp_Y + 1][temp_X - 1] == 'r' or b_grid[temp_Y + 1][temp_X - 1] == 'R') and (current_player == (player_2))):
                    if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                        must_take3 = True

            else:
                if ((b_grid[temp_Y][temp_X]) == (player_1K)):
                    if ((b_grid[temp_Y + 1][temp_X - 1] == 'b' or b_grid[temp_Y + 1][temp_X - 1]  ==  'B') and (current_king == (player_1K))):
                        if (b_grid[temp_Y + 2][temp_X - 2] == ' '):
                            must_take3 = True

    #for must_take4
    if (temp_Y <= 5 and temp_X <= 5): #must stay in grid after moving
        if (current_player == (player_2) or current_king == (player_1K)):
            if (b_grid[temp_Y][temp_X] == (player_2) or b_grid[temp_Y][temp_X] == (player_2K)):
                if ((b_grid[temp_Y + 1][temp_X + 1] == 'r' or b_grid[temp_Y + 1][temp_X + 1] == 'R') and (current_player == (player_2))):
                    if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                        must_take4 = True

            elif (b_grid[temp_Y][temp_X] == (player_1) or b_grid[temp_Y][temp_X] == (player_1K)):
                if ((b_grid[temp_Y + 1][temp_X + 1] == 'b' or b_grid[temp_Y + 1][temp_X + 1] == 'B') and (current_king == (player_1K))):
                    if (b_grid[temp_Y + 2][temp_X + 2] == ' '):
                        must_take4 = True


    if (must_take1 == True or must_take2 == True or must_take3 == True or must_take4 == True): #if one of the statements are true
        ai_take = []

        #print out options that can be taken
        if (must_take1 == True):
            user_take = "1"
            ai_take.append(str(temp_X)+','+str(temp_Y))

        if (must_take2 == True):
            user_take = "2"
            ai_take.append(str(temp_X)+','+str(temp_Y))

        if (must_take3 == True):
            user_take = "3"
            ai_take.append(str(temp_X)+','+str(temp_Y))

        if (must_take4 == True):
            user_take = "4"
            ai_take.append(str(temp_X)+','+str(temp_Y))

        # ask user to choose an option depending on results
        if (user_take == "1" or user_take == "2" or user_take == "3" or user_take == "4"):

            #if the users choice matches with a statement which is true:
            if (must_take1 == True and user_take == "1"):
                if (temp_Y - 2 == 0):
                    b_grid[temp_Y - 2][temp_X - 2] = (current_king)
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y - 1][temp_X - 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 1\n")
                    additional_takes(temp_Y - 2, temp_X - 2) #call function again using new space
                else:
                    b_grid[temp_Y - 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y - 1][temp_X - 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 1\n")
                    additional_takes(temp_Y - 2, temp_X - 2)

            elif (must_take2 == True and user_take == "2"):
                if (temp_Y - 2 == 0):
                    b_grid[temp_Y - 2][temp_X + 2] = (current_king)
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y - 1][temp_X + 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 2\n")
                    additional_takes(temp_Y - 2, temp_X + 2)
                else:
                    b_grid[temp_Y - 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y - 1][temp_X + 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 2\n")
                    additional_takes(temp_Y - 2, temp_X + 2)

            elif (must_take3 == True and user_take == '3'):
                if (temp_Y + 2 == 7):
                    b_grid[temp_Y + 2][temp_X - 2] = (current_king)
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y + 1][temp_X - 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 3\n")
                    additional_takes(temp_Y + 2, temp_X - 2)
                else:
                    b_grid[temp_Y + 2][temp_X - 2] = b_grid[temp_Y][temp_X]
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y + 1][temp_X - 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 3\n")
                    additional_takes(temp_Y + 2, temp_X - 2)

            elif (must_take4 == True and user_take == '4'):
                if (temp_Y + 2 == 7):
                    b_grid[temp_Y + 2][temp_X + 2] = (current_king)
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y + 1][temp_X + 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 4\n")
                    additional_takes(temp_Y + 2, temp_X + 2)
                else:
                    b_grid[temp_Y + 2][temp_X + 2] = b_grid[temp_Y][temp_X]
                    b_grid[temp_Y][temp_X] = (' ')
                    b_grid[temp_Y + 1][temp_X + 1] = (' ')
                    print ("There was another piece to be taken at", str(temp_X)+","+str(temp_Y))
                    print ("In direction: 4\n")
                    additional_takes(temp_Y + 2, temp_X + 2)

    #reset variables to be false
    must_take1 = False
    must_take2 = False
    must_take3 = False
    must_take4 = False

#get coord for moving a piece
def get_input():
    global split_fromX, split_fromY, move_from

    if (against_ai == True): #if against ai
        if (current_player == player_2):
            move_from = ai_selected
        else:
            print("\nPlease enter the co-ordinates of the piece you would like to move\n('cancel' to exit): ")
            move_from = input("> ") #input co-ord to move from

        while (len(move_from) != 3): #keep looping until string meets requirements
            if (move_from == ''): #allow out of loop
                print ("Please enter in the format 'x,y': \n")
                make_move()

            elif (move_from == "check"):
                print ("\n\nCurrent turn: " + str(move_turn))
                print ("Current player: " + str(current_player)+ "\n")
                print_grid()

            elif (move_from == 'exit'): #if player wants to quit
                print ("\n** Thanks for playing! **\n")
                sys.exit()

            #ask user to reinput co-ords
            print ("\nPlease enter in the format 'x,y': \n")
            coord_input = input("> ")
            if (len(coord_input) == 3 and coord_input[0].isnumeric() and coord_input[2].isnumeric() and coord_input[1] == ','): #if meets requirements then convert
                move_from = coord_input

            elif (coord_input == 'exit'): #allow user to quit
                print ("\n** Thanks for playing! **\n")
                sys.exit()

        else:
            if (len(move_from) == 3 and move_from[0].isnumeric() and move_from[2].isnumeric() and move_from[1] == ','):
                split_from = move_from.split(',') #var to split by comma (creates into array)
                split_fromX = int(split_from[0])
                split_fromY = int(split_from[1])
            else:
                get_input() #if conditions not met out of loop, go back to beginning
    else:
        print("\nPlease enter the co-ordinates of the piece you would like to move\n('cancel' to exit): ")
        move_from = input("> ") #input co-ord to move from

        while (len(move_from) != 3): #keep looping until string meets requirements
            if (move_from == ''): #allow out of loop
                print ("Please enter in the format 'x,y': ")
                make_move()

            elif (move_from == "check"):
                print ("\n\nCurrent turn: " + str(move_turn))
                print ("Current player: " + str(current_player)+ "\n")
                print_grid()

            elif (move_from == 'exit'): #if player wants to quit
                print ("\n** Thanks for playing! **\n")
                sys.exit()

            #ask user to reinput co-ords
            print ("\nPlease enter in the format 'x,y': ")
            coord_input = input("> ")
            if (len(coord_input) == 3 and coord_input[0].isnumeric() and coord_input[2].isnumeric() and coord_input[1] == ','): #if meets requirements then convert
                move_from = coord_input

            elif (coord_input == 'exit'): #allow user to quit
                print ("\n** Thanks for playing! **\n")
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
    global current_player, move_to, split_fromY, split_fromX

    print ("\nPlease type the number of the direction you would like to move.")
    if (against_p2 == True):

        #if piece is King piece
        if (b_grid[split_fromY][split_fromX] == (player_1K) or b_grid[split_fromY][split_fromX] == (player_2K)):
            print ("1   2")
            print ("  "+ current_player +"  ")
            print ("3   4\n")

        #if piece is 'r'
        elif (b_grid[split_fromY][split_fromX] == (player_1)):
            print ("1   2")
            print ("  "+ current_player +"  ")
        else:
            if (b_grid[split_fromY][split_fromX] == 'b'):
                print ("  "+ current_player +"  ")
                print ("3   4\n")

        print ("Please enter your choice ('cancel to exit'): ")
        move_to = input("> ")
        if (move_to == "1" or move_to == "2" or move_to == "3" or move_to == "4"):
            pass
        else:
            print ("Not a valid option!\n")
            get_dir() #go back to beginning

    #if the current player is 2
    if (against_ai == True): #if against ai
        if (b_grid[split_fromY][split_fromX] == (player_1K) or b_grid[split_fromY][split_fromX] == (player_2K)):
            print ("1   2")
            print ("  "+ current_player +"  ")
            print ("3   4\n")

        #if piece is 'r'
        elif (b_grid[split_fromY][split_fromX] == (player_1)):
            print ("1   2")
            print ("  "+ current_player +"  ")

        if (current_player == player_2):
            if (b_grid[split_fromY][split_fromX] == player_2K): #if king piece
                if (b_grid[split_fromY - 1][split_fromX - 1] == ' '):
                    move_to = "1"
                    print ("Player 2 has chosen: 1\n")
                elif (b_grid[split_fromY - 1][split_fromX + 1] == ' '):
                    move_to = "2"
                    print ("Player 2 has chosen: 2\n")

            elif (b_grid[split_fromY][split_fromX] == player_2): # if normal piece
                if (b_grid[split_fromY + 1][split_fromX - 1] == ' '):
                    move_to = "3"
                    print ("Player 2 has chosen: 3\n")
                elif (b_grid[split_fromY + 1][split_fromX + 1] == ' '):
                    move_to = "4"
                    print ("Player 2 has chosen: 4\n")

        #if player's turn
        else:
            print ("Please enter your choice ('cancel to exit'): ")
            move_to = input("> ")
            if (move_to == "1" or move_to == "2" or move_to == "3" or move_to == "4"):
                pass
            else:
                print ("Not a valid option!\n")
                get_dir() #go back to beginning

#make a move
def make_move():
    global move_turn, split_fromX, split_fromY, move_to, current_player, current_king

    get_input()

    #check if coords are in grid
    if ((split_fromY) >= 0 and (split_fromY) <= 7 and (split_fromX) >= 0 and (split_fromX) <= 7):
        #check if oiece belongs to current player
        if (b_grid[split_fromY][split_fromX] == (current_player) or b_grid[split_fromY][split_fromX] == (current_king)):

            get_dir()#if meets requirements are met then get directon

            #if user chooses 1
            if (move_to == '1'):
                #only player 1 piece or AI King can move in direction 1
                if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R' or (b_grid[split_fromY][split_fromX]) == 'B'):
                    if ((split_fromY - 1 >= 0) and (split_fromX - 1 >= 0)): #check that space is in grid
                        if ((b_grid[split_fromY - 1][split_fromX - 1]) == ' '): # check if enemy piece
                            if (current_player == player_1):

                                #if the y co-ord is last row (0)
                                if ((split_fromY - 2) == 0):
                                    undo_grid = b_grid[:]
                                    undo_grid = copy.deepcopy(b_grid)
                                    b_grid[split_fromY - 1][split_fromX - 1] = (player_1K)
                                    b_grid[split_fromY][split_fromX] = ' '
                                    move_turn += 1 #update the turn

                                else:
                                    if (b_grid[split_fromY][split_fromX] == "r"):
                                        undo_grid = b_grid[:]
                                        undo_grid = copy.deepcopy(b_grid)
                                        b_grid[split_fromY - 1][split_fromX - 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1

                                    elif (b_grid[split_fromY][split_fromX] == "R"):
                                        undo_grid = b_grid[:]
                                        undo_grid = copy.deepcopy(b_grid)
                                        b_grid[split_fromY - 1][split_fromX - 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1

                            #if piece is ai piece and current player is ai
                            elif (current_player == player_2):
                                if (b_grid[split_fromY][split_fromX] == 'B'):
                                    undo_grid = b_grid[:]
                                    undo_grid = copy.deepcopy(b_grid)
                                    if ((b_grid[split_fromY - 1][split_fromX - 1]) == ' '):
                                            b_grid[split_fromY - 1][split_fromX - 1] = (player_2K)
                                            b_grid[split_fromY][split_fromX] = ' '

                        else:
                            print ("\n* You cannot move here! (No empty space) *\n")
                    else:
                        print ("\n* You cannot move here! (Out of grid) *\n")
                else:
                    print ("\n* This piece cannot move in that direction! (Only player 1 or King pieces) *\n")

            #if user chooses 2
            elif (move_to == '2'):
                #only player 1 piece or AI King can move in direction 2
                if ((b_grid[split_fromY][split_fromX]) == 'r' or (b_grid[split_fromY][split_fromX]) == 'R' or (b_grid[split_fromY][split_fromX]) == 'B'):
                    if ((split_fromY - 1) >= 0 and (split_fromX + 1) <= 7): #check that space is in grid
                        if (b_grid[split_fromY - 1][split_fromX + 1] == ' '): # check if enemy piece
                            if (current_player == player_1):

                                #if the y co-ord is last row (0)
                                if ((split_fromY - 1) == 0):
                                    b_grid[split_fromY - 1][split_fromX + 1] = (player_1K)
                                    b_grid[split_fromY][split_fromX] = ' '
                                    move_turn += 1 #update the turn

                                else:
                                    if (b_grid[split_fromY][split_fromX] == 'r'):
                                        b_grid[split_fromY - 1][split_fromX + 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                                    elif (b_grid[split_fromY][split_fromX] == 'R'):
                                        b_grid[split_fromY - 1][split_fromX + 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                            elif (current_player == player_2):
                                if (b_grid[split_fromY][split_fromX] == 'B'):
                                    b_grid[split_fromY - 1][split_fromX + 1] == b_grid[split_fromY][split_fromX]
                                    b_grid[split_fromY][split_fromX] == ' '
                                    move_turn += 1

                        else:
                            print ("\n* You cannot move here! (No empty space) *\n")
                    else:
                        print ("\n* You cannot move here! (Out of grid) *\n")
                else:
                    print ("\n* This piece cannot move in that direction! (Only player 1 or King pieces) *\n")

            #if user chooses 3
            elif (move_to == '3'):
                #only AI piece or player 1 King can move in direction 3
                if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B' or (b_grid[split_fromY][split_fromX]) == 'R'):
                    if ((split_fromY + 1) <= 7 and (split_fromX - 1) >= 0): #check that space is in grid
                        if ((b_grid[split_fromY + 1][split_fromX - 1]) == ' '): #if next space is empty
                            if (current_player == player_2):
                                if ((split_fromY + 1) == 7): #if end of row
                                    if ((b_grid[split_fromY][split_fromX]) == 'b'):
                                        b_grid[split_fromY + 1][split_fromX - 1] = (player_2K)
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1
                                else:
                                    if ((b_grid[split_fromY][split_fromX]) == 'b'):
                                        b_grid[split_fromY + 1][split_fromX - 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                                    elif ((b_grid[split_fromY][split_fromX]) == 'B'):
                                        b_grid[split_fromY + 1][split_fromX - 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                            elif (current_player == player_1):
                                if ((b_grid[split_fromY][split_fromX]) == 'R'): #if player piece
                                    b_grid[split_fromY + 1][split_fromX - 1] = b_grid[split_fromY][split_fromX]
                                    b_grid[split_fromY][split_fromX] = ' '
                                    move_turn += 1

                        else:
                            print ("\n* You cannot move there! (No empty space) *\n")
                    else:
                        print ("\n* You cannot move here! (Out of grid) *\n")
                else:
                    print ("\n* This piece cannot move in that direction! (Only AI or King pieces) *\n")

            #if user chooses 4
            elif (move_to == '4'):
                #only AI piece or player 1 King can move in direction 4
                if ((b_grid[split_fromY][split_fromX]) == 'b' or (b_grid[split_fromY][split_fromX]) == 'B' or (b_grid[split_fromY][split_fromX]) == 'R'):
                    if ((split_fromY + 1) <= 7 and (split_fromX + 1) <= 7): #check that space is in grid
                        if ((b_grid[split_fromY + 1][split_fromX + 1]) == ' '): # if next space is empty
                            if (current_player == player_2):

                                if ((split_fromY + 1) == 7): #if end of row
                                    if ((b_grid[split_fromY][split_fromX]) == 'b'):
                                        b_grid[split_fromY + 1][split_fromX + 1] = (player_2K)
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1

                                else:
                                    if ((b_grid[split_fromY][split_fromX]) == 'b'):
                                        b_grid[split_fromY + 1][split_fromX + 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                                    elif ((b_grid[split_fromY][split_fromX]) == 'B'):
                                        b_grid[split_fromY + 1][split_fromX + 1] = b_grid[split_fromY][split_fromX]
                                        b_grid[split_fromY][split_fromX] = ' '
                                        move_turn += 1 #update the turn

                            elif (current_player == player_1):
                                if ((b_grid[split_fromY][split_fromX]) == 'R'): #if player piece
                                    b_grid[split_fromY + 1][split_fromX + 1] = b_grid[split_fromY][split_fromX]
                                    b_grid[split_fromY][split_fromX] = ' '
                                    move_turn += 1
                        else:
                            print ("\n* You cannot move here! (No empty space) *\n")
                    else:
                        print ("\n* You cannot move here! (Out of grid) *\n")
                else:
                    print ("\n* This piece cannot move in that direction! (Only AI or King pieces) *\n")

            elif (move_to == "exit"):
                print ("\n** Thanks for playing! **\n")
                sys.exit()
        else:
            print ("\n* You do not have a piece here! *\n")
    else:
        print ("\n* This is not in the grid! *\n")

#ai function
def ai_select():
    global ai_selected, move_from, move_to, move_turn, split_fromX, split_fromY, current_player, current_king

    ai_X = 0
    ai_Y = 0
    ai_list = []

    for i in b_grid:
        for j in i:
            if (b_grid[ai_Y][ai_X] == player_2 or b_grid[ai_Y][ai_X] == player_2K): #if piece = player 2

                #if king piece and 1 is free
                if (ai_Y >= 1 and ai_X >= 1):
                    if (b_grid[ai_Y - 1][ai_X - 1] == (player_2K) and b_grid[ai_Y - 1][ai_X - 1] == ' '):
                        ai_list.append(str(ai_X)+","+str(ai_Y)) #add the coords to a list
                        ai_selected = random.choice(ai_list) #coords x,y is converted in get_input()

                #if king piece and 2 is free
                if (ai_Y >= 1 and ai_X <= 6):
                    if (b_grid[ai_Y - 1][ai_X + 1] == (player_2K) and b_grid[ai_Y - 1][ai_X + 1] == ' '):
                        ai_list.append(str(ai_X)+","+str(ai_Y))
                        ai_selected = random.choice(ai_list)

                #if 3 is free
                if (ai_Y <= 6 and ai_X >= 1):
                    if (b_grid[ai_Y + 1][ai_X - 1] == ' '):
                        ai_list.append(str(ai_X)+","+str(ai_Y))
                        ai_selected = random.choice(ai_list)

                #if 4 is free
                if (ai_Y <= 6 and ai_X <= 6):
                    if (b_grid[ai_Y + 1][ai_X + 1] == ' '):
                        ai_list.append(str(ai_X)+","+str(ai_Y))
                        ai_selected = random.choice(ai_list)

            ai_X += 1 #increment the X coord
            if (ai_X > 7): #if X coord is > 7 then reset to 0 for next row
                ai_X = 0
        ai_Y += 1 #increment Y coord

    print ("\nPlayer 2 has chosen: ", str(ai_selected)) #print what ai selects
    make_move()
    update_player()

# def history():

def undo():
    global move_turn, b_grid

    if (b_grid == undo_grid):
        print ("* Cannot undo any further! *\n")

    else:
        #confirm if user would like to undo
        print ("Would you like to undo (yes/no)?")
        yes_undo = input("> ")

        if (yes_undo == "yes"):
            print ("move undid lol")
            b_grid = undo_grid[:] #set grid to
            b_grid = copy.deepcopy(undo_grid)
            if move_turn == 1:
                pass
            else:
                move_turn -= 1
        elif (yes_undo == "exit"):
            print ("\n** Thanks for playing! **\n")
            sys.exit()

        else:
            pass

def redo():
    global move_turn, b_grid

    if (b_grid == redo_grid):
        print ("* Cannot redo any further! *\n")

    else:
        #confirm if user would like to undo
        print ("Would you like to redo (yes/no)?")
        yes_redo = input("> ")

        if (yes_redo == "yes"):
            print ("move redid lol")
            b_grid = redo_grid[:] #set grid to new grid
            b_grid = copy.deepcopy(redo_grid)
            move_turn += 1

        elif (yes_redo == "exit"):
            print ("\n** Thanks for playing! **\n")
            sys.exit()
        else:
            pass

#determine the results
def results():
    p1_in_grid = False #if p1 is still in the grid
    p2_in_grid = False #if p2 is still in the grid

    for i in b_grid:
        for j in i:
            #check grid for any player 1 pieces
            if (j == player_1 or j == player_1K):
                p1_in_grid = True #if piece found, set var to true

            #check grid for any player 2 pieces
            if (j == player_2 or j == player_2K):
                p2_in_grid = True

    #if player 1 piece in grid and player 2 piece is not then player 1 wins
    if (p2_in_grid == False and p1_in_grid == True):
        print("\nPlayer 1 wins\n")
        print ("** Thanks for playing! **\n")
        sys.exit()

    #if player 2 piece in grid and player 1 piece is not then player 2 wins
    if (p1_in_grid == False and p2_in_grid == True):
        print("\nPlayer 2 wins\n")
        print ("** Thanks for playing! **\n")
        sys.exit()

########
# GAME #
########

print ("\n** Now playing: Checkers! **\n")
startup_rules()

user_input = input("Please press enter to start: \n")

ai_p2() #ask user what mode to play in

while (user_input != 'exit'):
    print ("\n\nCurrent turn: " + str(move_turn))
    print ("Current player: " + str(current_player)+ "\n")
    print_grid()
    results()

    piece_moved = False

    if (against_ai == True and against_p2 == False):
        #before user can choose to move piece, check for pieces which must be moved
        mandatory_take()

        if (piece_moved == False): #checks if a piece has been moved this turn
            #to start game, move a piece
            if (current_player == player_1):
                print ("Type 'move' to move a piece")
                user_input = input("> ")

                if (user_input == 'rules'):
                    rules()

                #if user wants to move a piece
                elif (user_input == 'move'):
                    undo_grid = b_grid[:] #save the previous state
                    undo_grid = copy.deepcopy(b_grid)
                    make_move()
                    update_player()
                    redo_grid = b_grid[:] #save the current state
                    redo_grid = copy.deepcopy(b_grid)

                #if user wants to see rules
                elif (user_input == 'check'):
                    print ("\nCurrent turn: " + str(move_turn))
                    print ("Current player: " + str(current_player)+ "\n")
                    print_grid()

                #if user wants to undo a move
                elif (user_input == "undo"):
                    undo()
                    print ("\n* Move undone!*\n")

                #if the user want to redo a move
                elif (user_input == "redo"):
                    redo()
                    print ("\n* Move redone! *\n")

                elif (user_input == '' or user_input == ' '):
                    print ("\nPlease enter your choice!\n")

                elif (user_input == 'exit'):
                    break

                else:
                    print ("\nPlease re-enter your choice.\n")
            else:
                ai_select()
        else:
            pass

    elif (against_p2 == True and against_ai == False):
        #before user can choose to move piece, check for pieces which must be moved

        print ("undo:", undo_grid)
        mandatory_take()
        redo_grid = b_grid[:]
        redo_grid = copy.deepcopy(b_grid)
        # print ("redo: ", redo_grid)

        if (piece_moved == False): #checks if a piece has been moved this turn
            #to start game, move a piece
            print ("Type 'move' to move a piece")
            user_input = input("> ")

            if (user_input == 'rules'):
                rules()

            #if user wants to move a piece
            elif (user_input == 'move'):
                undo_grid = b_grid[:] #save the previous state
                undo_grid = copy.deepcopy(b_grid)
                make_move()
                update_player()
                redo_grid = b_grid[:] #save the current state
                redo_grid = copy.deepcopy(b_grid)

            #if user wants to see rules
            elif (user_input == 'check'):
                print ("\nCurrent turn: " + str(move_turn))
                print ("Current player: " + str(current_player)+ "\n")
                print_grid()

            #if user wants to undo a move
            elif (user_input == "undo"):
                undo()

            #if the user want to redo a move
            elif (user_input == "redo"):
                redo()

            elif (user_input == '' or user_input == ' '):
                print ("\nPlease enter your choice!\n")

            else:
                print ("\nPlease re-enter your choice.\n")
        else:
             pass

else:
    sys.exit() #if user quits

#when game ends
print ("\n** Thanks for playing! **\n")
