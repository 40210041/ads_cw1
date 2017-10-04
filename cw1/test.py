#test.py
#used for testing stufffff


p_1 = "x"
p_2 = "o"
p1_win = "Player 1 wins!"
p2_win = "Player 2 wins!"
this_player = ""
move_turn = 0
user_move = input()

#make the grid
b_grid = [[' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']]

#define a function to build board via print
def print_grid():
    print ("your board:")
    print (" "+b_grid[0][0]+" | "+b_grid[0][1]+" | "+b_grid[0][2]+" ")
    print ("-----------")
    print (" "+b_grid[1][0]+" | "+b_grid[1][1]+" | "+b_grid[1][2]+" ")
    print ("-----------")
    print (" "+b_grid[2][0]+" | "+b_grid[2][1]+" | "+b_grid[2][2]+" ")

def p1_p2():
    if move_turn % 2 == 0:
        this_player = p_2
    else:
        this_player = p_1
    print (this_player)

# def results():
#     if ((b_grid[0][0] and b_grid[0][1] and b_grid[0][2] != " ")and
#         (b_grid[1][0] and b_grid[1][1] and b_grid[1][2] != " ")and
#         (b_grid[2][0] and b_grid[2][1] and b_grid[2][2] != " ")):
#         print ("Its a draw fam")
#         user_move = ("exit")
#         break
#
#     if ((b_grid[0][0] and b_grid[0][1] and b_grid[0][2] == p_1) or
#         (b_grid[1][0] and b_grid[1][1] and b_grid[1][2] == p_1) or
#         (b_grid[2][0] and b_grid[2][1] and b_grid[2][2] == p_1) or
#         (b_grid[0][0] and b_grid[1][0] and b_grid[2][0] == p_1) or
#         (b_grid[0][1] and b_grid[1][1] and b_grid[2][1] == p_1) or
#         (b_grid[0][2] and b_grid[1][2] and b_grid[2][2] == p_1) or
#         (b_grid[0][0] and b_grid[1][1] and b_grid[2][2] == p_1) or
#         (b_grid[0][2] and b_grid[1][1] and b_grid[2][0] == p_1)):
#         print ("Player 1 wins!")
#         user_move = ("exit")
#         break
#
#     if ((b_grid[0][0] and b_grid[0][1] and b_grid[0][2] == p_2) or
#         (b_grid[1][0] and b_grid[1][1] and b_grid[1][2] == p_2) or
#         (b_grid[2][0] and b_grid[2][1] and b_grid[2][2] == p_2) or
#         (b_grid[0][0] and b_grid[1][0] and b_grid[2][0] == p_2) or
#         (b_grid[0][1] and b_grid[1][1] and b_grid[2][1] == p_2) or
#         (b_grid[0][2] and b_grid[1][2] and b_grid[2][2] == p_2) or
#         (b_grid[0][0] and b_grid[1][1] and b_grid[2][2] == p_2) or
#         (b_grid[0][2] and b_grid[1][1] and b_grid[2][0] == p_2)):
#         print ("Player 1 wins!")
#         user_move = ("exit")
#         break

############
### GAME ###
############

#setup vars

#while loop, allow user to quit with "exit"
#put user input into
while (user_move != "exit"):
    print_grid()
    if ((b_grid[0][0] != " " and b_grid[0][1] != " " and b_grid[0][2] != " ")and
        (b_grid[1][0] != " " and b_grid[1][1] != " " and b_grid[1][2] != " ")and
        (b_grid[2][0] != " " and b_grid[2][1] != " " and b_grid[2][2] != " ")):
        print ("Its a draw fam")
        user_move = ("exit")
        break

    if ((b_grid[0][0] == p_1 and b_grid[0][1] == p_1 and b_grid[0][2] == p_1) or
        (b_grid[1][0] == p_1 and b_grid[1][1] == p_1 and b_grid[1][2] == p_1) or
        (b_grid[2][0] == p_1 and b_grid[2][1] == p_1 and b_grid[2][2] == p_1) or
        (b_grid[0][0] == p_1 and b_grid[1][0] == p_1 and b_grid[2][0] == p_1) or
        (b_grid[0][1] == p_1 and b_grid[1][1] == p_1 and b_grid[2][1] == p_1) or
        (b_grid[0][2] == p_1 and b_grid[1][2] == p_1 and b_grid[2][2] == p_1) or
        (b_grid[0][0] == p_1 and b_grid[1][1] == p_1 and b_grid[2][2] == p_1) or
        (b_grid[0][2] == p_1 and b_grid[1][1] == p_1 and b_grid[2][0] == p_1)):
        print ("Player 1 wins!")
        user_move = ("exit")
        break

    if ((b_grid[0][0] == p_2 and b_grid[0][1] == p_2 and b_grid[0][2] == p_2) or
        (b_grid[1][0] == p_2 and b_grid[1][1] == p_2 and b_grid[1][2] == p_2) or
        (b_grid[2][0] == p_2 and b_grid[2][1] == p_2 and b_grid[2][2] == p_2) or
        (b_grid[0][0] == p_2 and b_grid[1][0] == p_2 and b_grid[2][0] == p_2) or
        (b_grid[0][1] == p_2 and b_grid[1][1] == p_2 and b_grid[2][1] == p_2) or
        (b_grid[0][2] == p_2 and b_grid[1][2] == p_2 and b_grid[2][2] == p_2) or
        (b_grid[0][0] == p_2 and b_grid[1][1] == p_2 and b_grid[2][2] == p_2) or
        (b_grid[0][2] == p_2 and b_grid[1][1] == p_2 and b_grid[2][0] == p_2)):
        print ("Player 1 wins!")
        user_move = ("exit")
        break

    user_move = input("> ")
    if user_move == ("1"):
        if b_grid[0][0] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[0][0] = this_player
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("2"):
        if b_grid[0][1] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[0][1] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("3"):
        if b_grid[0][2] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[0][2] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("4"):
        if b_grid[1][0] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[1][0] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("5"):
        if b_grid[1][1] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[1][1] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("6"):
        if b_grid[1][2] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[1][2] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("7"):
        if b_grid[2][0] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[2][0] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("8"):
        if b_grid[2][1] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[2][1] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    elif user_move == ("9"):
        if b_grid[2][2] == (" "):
            move_turn += 1
            if move_turn % 2 == 0:
                this_player = p_2
            else:
                this_player = p_1
            b_grid[2][2] = (this_player)
        else:
            print("thats been  T A K E N\nchoose another space pls\n")
    else:
        break
    print ("Current player:", (this_player))
    print ("Current turn:", str(move_turn))
 #""MOVE TURN"" :)))))))))
    #imlement counter to be shown at end

#winning lines
#(1,2,3) (4,5,6) (7,8,9)
#(1,4,7) (2,5,8) (3,6,9)
#(1,5,9) (3,5,7)

#store score
#winners.append(winner)

#please let me pass this year thank u
