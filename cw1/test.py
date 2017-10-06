#test.py

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
user_input = input("Please press enter to start:")

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
######### add how to move pieces too!! ########
def startup_rules():
    print ("Type 'rules' for rules.")
    print ("Type 'exit' to quit.\n")
    print ("Aim to remove all of the opponents pieces!")
    print ("Enter the co-ordinates of the piece you would like to move.")
    # print ("Type 1 to move upwards left.")
    # print ("Type 2 to move upwards right.")
    # print ("3 and 4 *King only!*")
    print ("1   2\n  "+current_player+"   \n3   4")

def rules():
    print ("\n* RULES *")
    print ("• Player 1 is Red, Player 2 is Black.")
    print ("• Move the pieces diagonally forward to remove the other players pieces.")
    print ("• Moving a piece to the opponents side will make that piece into a King.")
    print ("• King pieces can move back and forth diagonally.\n")

#print board
#create a loop to print out board using i
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

print ("Hello World!\n")

while (user_input != 'exit'):
    print_grid()

    user_input = input("> ")
    if user_input == 'rules':
        rules()
    elif user_input == 'move':
        print("Please enter the co-ordinates of the piece you would like to move:")
        from_piece = input("> ")
    elif user_input == '2':
        print ("\nhaha farewell\n")
    else:
        break
print ("\nThanks for playing!\n")
