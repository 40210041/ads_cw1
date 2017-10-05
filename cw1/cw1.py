#cw1.py
#create a game like checkers

# Your game should record play history, i.e. the sequence of moves that the players make during a game,
# so that each game that is played can be recorded and replayed.
# Your game should support undo and redo, again selecting the most appropriate data structures
# to enable these functionalities.
# Finally, your game should implement an algorithm that enables the computer to choose
# which moves to make during their own turn, i.e. a simple AI player. Your choice
# of algorithm for the AI player may be from the literature, or of your own design. Whichever your
# choice you must be able to evaluate and justify your selection of both data structures and algorithms.
# The game should run from the command line, using a text based interface in the first instance.

# PLS LET ME PASS LOL

##########
# SETUP #
#########

#http://www.darkfish.com/checkers/rules.html (rules)

#setup vars
player_1 = "r"
player_2 = "b"
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


#define functions

#print out the rules
def rules():
    print ("\n* RULES *")
    print ("• Player 1 is Red, Player 2 is Black.")
    print ("• Aim to remove all of the other players pieces.")
    print ("• Move the pieces diagonally forward to remove the other players pieces.")
    print ("• Moving a piece to the opponents side will make that piece into a King.")
    print ("• King pieces can move back and forth diagonally.\n"
    )

#print board
#create a loop to print out board using i
def print_grid():
    print ("  +-------------------------------+")
    i = 0
    j = 0
    #print same lines 8 times, i increments by 1 each loop
    while i < len(b_grid):
        print (str(j) + " | "+b_grid[i][0]+" | "+b_grid[i][1]+" | "+b_grid[i][2]+" | "+b_grid[i][3]+" | "+b_grid[i][4]+" | "+b_grid[i][5]+" | "+b_grid[i][6]+" | "+b_grid[i][7]+ " |")
        print ("  +-------------------------------+")
        i += 1
        j += 1
    print (" 0   1   2   3   4   5   6   7 ")

########
# GAME #
########

print ("Hello World!\n")
print_grid()
rules()
print ("End of program!\n")
