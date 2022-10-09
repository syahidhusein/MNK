import numpy as np
import random
import time

"""
MNK game is a two-player game similar to Tic Tac Toe but with a MxN board with K amount of letters in a row to win.
Our version is the M = 5, N = 5, and K = 4 version.
How the game works : 1. Each player picks their letter, either X or O and one of them starts the game.
                     2. First player places their letter anywhere on the board they desire.
                     3. Second player places does the same but with their corresponding letter.
                     4. The take turns alternating with one another until one of them is able to have 4 of their letters in a row; either
                        horizontally,vertically or diagonally.
"""

game_board = np.array([["-" , "-" , "-" , "-" , "-"],
                       ["-" , "-" , "-" , "-" , "-"],
                       ["-" , "-" , "-" , "-" , "-"],
                       ["-" , "-" , "-" , "-" , "-"],
                       ["-" , "-" , "-" , "-" , "-"]])

game_over = False
counter = 0         #for draw condition, if it reach 25 (max possible moves)
skip_action = False #extra step for regular/smart com, preventing double move at a time


def print_board(board):
    """
    Prints the MNK board; in our case, a 5x5 board.
    Each position on the board, however, is indexed with our numpy array (game_board) above.
    """

    
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|" + board[0][3] + "|" + board[0][4])
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" + board[1][3] + "|" + board[1][4])
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" + board[2][3] + "|" + board[2][4])
    print(board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" + board[3][3] + "|" + board[3][4])
    print(board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" + board[4][3] + "|" + board[4][4])


def game_decider(board):
    """
    game_decider(board) : A single function that runs its inner functions to check for winning condition for the user.
    winning condition : 4 of the same letter in a row. Each function checks if the first,second,third and fourth string are the same string.
    Inner Functions:
    1. Check_Row(board) : a) Checks for winning condition in a horizontal row. If winning condition is met, it ends the game and reveals the winner.
                          b) With the help of numpy, the board is transposed on its horizontal (game_board.T) so that the vertical columns are now horizontal rows.
                             With this, the same Check_Row(board) function can be used to check for winning condition in the vertical columns.
    2. Check_Positive_Diagonal(board) and Check_Negative_Diagonal(board) : Checks for winning conditions along the diagonal.
                                                                           (Positive signifies a diagonal of positive gradient,
                                                                           Negative signifies a diagonal of negative gradient.)
    """

    
    
    def Check_Row(board):
        global game_over
        for i in range(5):
            if (board[i][0] == "X") and ((board[i][0] == board[i][1] == board[i][2] == board[i][3]) ):
                print("Player X wins")
                game_over = True
                
            elif (board[i][1] == "X") and ((board[i][1] == board[i][2] == board[i][3] == board[i][4])):
                print("Player X wins")
                game_over = True
                
            if (board[i][1] == "O") and ((board[i][0] == board[i][1] == board[i][2] == board[i][3])):
                print("Player O wins")
                game_over = True
                
            elif (board[i][1] == "O") and ((board[i][1] == board[i][2] == board[i][3] == board[i][4])):
                print("Player O wins")
                game_over = True
                
            
    def Check_Positive_Diagonal(board):
        global game_over
        if ((board[0][3]) == "X") and ((board[0][3] == board[1][2] == board[2][1] == board[3][0])):
            print("Player X wins")
            game_over = True
            
        elif ((board[1][4]) == "X") and ((board[1][4] == board[2][3] == board[3][2] == board[4][1])):
            print("Player X wins")
            game_over = True
            
        elif ((board[0][4]) == "X") and ((board[0][4] == board[1][3] == board[2][2] == board[3][1])):
            print("Player X wins")
            game_over = True
            
        elif ((board[1][3]) == "X") and ((board[1][3] == board[2][2] == board[3][1] == board[4][0])):
            print("Player X wins")
            game_over = True
            
        if ((board[0][3]) == "O") and ((board[0][3] == board[1][2] == board[2][1] == board[3][0])):
            print("Player O wins")
            game_over = True
            
        elif ((board[1][4]) == "O") and ((board[1][4] == board[2][3] == board[3][2] == board[4][1])):
            print("Player O wins")
            game_over = True
            
        elif ((board[0][4]) == "O") and ((board[0][4] == board[1][3] == board[2][2] == board[3][1])):
            print("Player O wins")
            game_over = True
            
        elif ((board[1][3]) == "O") and ((board[1][3] == board[2][2] == board[3][1] == board[4][0])):
            print("Player O wins")
            game_over = True
            
        
    def Check_Negative_Diagonal(board):
        global game_over
        if ((board[1][0]) == "X") and ((board[1][0] == board[2][1] == board[3][2] == board[4][3])):
            print("Player X wins")
            game_over = True
            
        elif ((board[0][1]) == "X") and ((board[0][1] == board[1][2] == board[2][3] == board[3][4])):
            print("Player X wins")
            game_over = True
            return game_over
        elif ((board[0][0]) == "X") and ((board[0][0] == board[1][1] == board[2][2] == board[3][3])):
            print("Player X wins")
            game_over = True
            
        elif ((board[1][1]) == "X") and ((board[1][1] == board[2][2] == board[3][3] == board[4][4])):
            print("Player X wins")
            game_over = True
            
        if ((board[1][0]) == "O") and ((board[1][0] == board[2][1] == board[3][2] == board[4][3])):
            print("Player O wins")
            game_over = True
            
        elif ((board[0][1]) == "O") and ((board[0][1] == board[1][2] == board[2][3] == board[3][4])):
            print("Player O wins")
            game_over = True
            
        elif ((board[0][0]) == "O") and ((board[0][0] == board[1][1] == board[2][2] == board[3][3])):
            print("Player O wins")
            game_over = True
            
        elif ((board[1][1]) == "O") and ((board[1][1] == board[2][2] == board[3][3] == board[4][4])):
            print("Player O wins")
            game_over = True
                
    Check_Row(board)
    Check_Row(board.T) #Check for column with transpose of board
    Check_Positive_Diagonal(board)
    Check_Negative_Diagonal(board)


def player_move(playerXO):
    """
    A 'move' function for the player (either X or O). 
    1. Prompts user for input of position to place their letter, by row and column.
    2. The input goes through 3 layers of if conditions:
        a) The first if : checks if the inputs are digits. If they're not, it returns "Please enter number only!"
        b) The second if : checks if the inputs are within the limits of the 5x5 baord. If the input is somewhere outside the box, it returns
                           "Invalid move."
        c) The third if : checks whether or not the position requested is empty. If its already taken, it returns
                          "Move already made. Find another box."
        """
    
    global game_board 
    while True:
        input_row = input(f"Player {playerXO}, row?:\n")
        input_col = input(f"Player {playerXO}, column?:\n")
        if input_row.isdigit() and input_col.isdigit():
            row = int(input_row) - 1
            col = int(input_col) - 1
            if 0 <= row < 5 and 0 <= col < 5:
                if game_board[row][col] == "-":
                    game_board[row][col] = playerXO
                    break
                else:
                    print("Move already made. Find another box")
            else:
                print("Invalid move.")
        else:
            print("Please enter number only!")


def test_game():
    """
    A game function that tests out the flow of the game.
    1. A global Boolean variable, game_over, is set earlier as False as a to-be-manipulated variable inside our game_decider function.
    2. The game functions are packed inside a while loop, with the condition that meets the initial game_over == False variable.
    3. Within the game_decider function above, the Boolean variable game_over is changed to True when winning condition is met.
       This means that is the winning condition is met, the Boolean value of game_over no longer satisfies the condition of the while loop, the game ends.
    4. Within the while loop of the game, a counter is also set for the condition of a draw.
       (If 25 moves have been made by both players combined, that means all 25 spots have been filled, which results in a draw.)

       **print("\n") is added for cosmetic purposes, to give space between old and new printed board.

    """  
    global game_over
    print_board(game_board)
    counter = 0
    while game_over == False:
        player_move("X")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1
        if game_over:
            break
        elif counter == 25: #condition for draw
            game_over = True
            print("Game Draw")
            break
        player_move("O")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1

#test_game()


def random_comp_move(botXO):
    """
    A 'move' function for easy BOT (O or X)
    1. Similar while loop from player_move is applied, but with the rows and columns randomized with import random.
    (random.randint(0,4)
    2. The BOT also checks if the random position generated is occupied or not, if yes, it generates another random position until it is able to
       complete a move.
    """

    
    global game_board
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        #if col < 5 and row < 5:
        if game_board[row][col] == "-":
            game_board[row][col] = botXO
            break

def test_game_vs_com():
    """
    A game function VS easy BOT
    1. A global Boolean variable, game_over, is set earlier as False as a to-be-manipulated variable inside our game_decider function.
    2. The game functions are packed inside a while loop, with the condition that meets the initial game_over == False variable.
    3. Within the game_decider function above, the Boolean variable game_over is changed to True when winning condition is met.
       This means that is the winning condition is met, the Boolean value of game_over no longer satisfies the condition of the while loop, the game ends.
    4. Within the while loop of the game, a counter is also set for the condition of a draw.
       (If 25 moves have been made by both players combined, that means all 25 spots have been filled, which results in a draw.)
    5. Create a simple toss using random module, to give chance for both player or com to get the first move.

       **print("\n") is added for cosmetic purposes, to give space between old and new printed board.
       **time.sleep is used as a short delay to make for a better game experience.
    """
    # global game_board
    # global game_over
    # global counter
    
    def player_moves_first():
        global game_board
        global game_over
        global counter
        print_board(game_board)
        while game_over == False:
            player_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25: #condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            random_comp_move("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
        
    def comp_moves_first():
        global game_board
        global game_over
        global counter
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            random_comp_move("O")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25: #condition for draw
                game_over = True
                print("Game Draw")
                break
            player_move("X")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
        
    player_toss = random.randint(0, 10)
    AI_toss = random.randint(0, 10)
    if player_toss > AI_toss :
        print("\n" + "player starts first" + "\n")
        player_moves_first()
    else:
        print("\n" + "BOT starts first" + "\n")
        comp_moves_first()
        

# test_game_vs_com()

def test_game_com_vs_com():
    """
    A game function of easy BOT (X) vs easy BOT (O)

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    """
    
    global game_over
    global counter
    print_board(game_board)
    while game_over == False:
        time.sleep(2)
        random_comp_move("X")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1
        if game_over:
            break
        elif counter == 25: #condition for draw
            game_over = True
            print("Game Draw")
            break
        time.sleep(2)
        random_comp_move("O")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1

        
#test_game_com_vs_com()

def special_comp_move(botXO):
    """
    Designated move for COM to conquer the middle box at early stage of the game.
    Reason: To conquer the middle board and increase the chance to win
    
    If all the conditions are not met, then COM will start to create random move.
    """
    def conquer_move():
        global game_board
        while True:
            row = random.randint(1, 3)
            col = random.randint(1, 3)
            if game_board[row][col] == "-":
                game_board[row][col] = botXO
                break
            
    if game_board[2][2] == "-":
        game_board[2][2] = botXO
        
    elif counter <= 8:
        conquer_move()
    else:
        random_comp_move(botXO)
        
def smart_comp(botXO):
    """
    Special designated move for AI.
        - Scanning the board and check for possible win/lose situation.
        - If the condition is met, a necessary move should be registered
        - Use of "skip_action" to ensure only one move is registered at a time.
    
    The possible win or lose situation could be:
        OOO + _ or XXX + _ ,
        OO_ + O or XX_ + X ,
        in any variations of horizontal, vertical or diagonal.
        
    The AI should create a move/block opponent move in the middle of the board
    to create advantage.
    
    The loop scan for O then X, according to its movement hierachy:
        1) Winning move
        2) Blocking opponent's win move
        3) Create advantage move
        4) Block advantage move
        5) Regular move
    
    """
    global game_board
    board_col = game_board.T

    def row_move(board,playerXO):
        global skip_action
        for i in range(5):
            #condition for 3 in a row
            if (board[i][0] == playerXO) and ((board[i][0] == board[i][1] == board[i][2])):
                if board[i][3] == "-":
                    board[i][3] = botXO
                    skip_action = True
                    return True

            elif (board[i][1] == playerXO) and ((board[i][1] == board[i][2] == board[i][3])):
                if board[i][4] == "-":
                    board[i][4] = botXO
                    skip_action = True
                    return True
                    
                elif board[i][0] == "-":
                    board[i][0] = botXO
                    skip_action = True
                    return True


            elif (board[i][2] == playerXO) and ((board[i][2] == board[i][3] == board[i][4])):
                if board[i][1] == "-":
                    board[i][1] = botXO
                    skip_action = True
                    return True
                    
    def row_move2(board, playerXO):
        global skip_action
        for i in range(5):
        #condition for 2 in a row        
            if (board[i][0] == playerXO) and ((board[i][0] == board[i][2] == board[i][3])):
                if board[i][1] == "-":
                    board[i][1] = botXO
                    skip_action = True
                    return True
                    
            elif (board[i][1] == playerXO) and ((board[i][1] == board[i][3] == board[i][4])):
                if board[i][2] == "-":
                    board[i][2] = botXO
                    skip_action = True
                    return True
            
            elif (board[i][3] == playerXO) and ((board[i][0] == board[i][1] == board[i][3])):
                if board[i][2] == "-":
                    board[i][2] = botXO
                    skip_action = True
                    return True
            
            elif (board[i][4] == playerXO) and ((board[i][1] == board[i][2] == board[i][4])):
                if board[i][3] == "-":
                    board[i][3] = botXO
                    skip_action = True
                    return True
    
    def diagonal_move(board, playerXO):
        global skip_action 
            #condition for 3 in a row
        if (board[2][2] == playerXO) and ((board[0][4] == board[1][3] == board[2][2])):
            if board[3][1] == "-":
                board[3][1] = botXO
                skip_action = True
                return True

        elif (board[2][2] == playerXO) and ((board[2][2] == board[1][3] == board[3][1])):
            if board[0][4] == "-":
                board[0][4] = botXO
                skip_action = True
                return True
                
            elif board[4][0] == "-":
                board[4][0] = botXO
                skip_action = True
                return True
            
        elif (board[2][2] == playerXO) and ((board[2][2] == board[3][1] == board[4][0])):
            if board[1][3] == "-":
                board[1][3] = botXO
                skip_action = True
                return True
            
        elif (board[2][3] == playerXO) and ((board[2][3] == board[3][2] == board[1][4])):
            if board[3][1] == "-":
                board[3][1] = botXO
                skip_action = True
                return True
            
        elif (board[2][3] == playerXO) and ((board[2][3] == board[3][2] == board[4][1])):
            if board[1][4] == "-":
                board[1][4] = botXO
                skip_action = True
                return True

        elif (board[2][1] == playerXO) and ((board[2][1] == board[1][2] == board[3][0])):
            if board[0][3] == "-":
                board[0][3] = botXO
                skip_action = True
                return True
            
        elif (board[2][1] == playerXO) and ((board[2][1] == board[1][2] == board[0][3])):
            if board[3][0] == "-":
                board[3][0] = botXO
                skip_action = True
                return True
            
    def another_diagonal_move(board, playerXO):
        global skip_action 
            #condition for 3 in a row
        if (board[2][2] == playerXO) and ((board[0][0] == board[1][1] == board[2][2])):
            if board[3][3] == "-":
                board[3][3] = botXO
                skip_action = True
                return True

        elif (board[2][2] == playerXO) and ((board[2][2] == board[1][1] == board[3][3])):
            if board[0][0] == "-":
                board[0][0] = botXO
                skip_action = True
                return True
                
            elif board[4][4] == "-":
                board[4][4] = botXO
                skip_action = True
                return True
            
        elif (board[2][2] == playerXO) and ((board[2][2] == board[3][3] == board[4][4])):
            if board[1][1] == "-":
                board[1][1] = botXO
                skip_action = True
                return True

        elif (board[2][1] == playerXO) and ((board[2][1] == board[3][2] == board[4][3])):
            if board[1][0] == "-":
                board[1][0] = botXO
                skip_action = True
                return True
            
        elif (board[2][1] == playerXO) and ((board[2][1] == board[3][2] == board[1][0])):
            if board[4][3] == "-":
                board[4][3] = botXO
                skip_action = True
                return True

        elif (board[2][3] == playerXO) and ((board[2][3] == board[1][2] == board[3][4])):
            if board[0][1] == "-":
                board[0][1] = botXO
                skip_action = True
                return True
            
        elif (board[2][3] == playerXO) and ((board[2][3] == board[1][2] == board[0][1])):
            if board[3][4] == "-":
                board[3][4] = botXO
                skip_action = True
                return True
            
    def diagonal_move2(board, playerXO):
        global skip_action 
            #condition for 2 in a row + 1
        if (board[2][2] == playerXO) and ((board[2][2] == board[1][3] == board[4][0])):
            if board[3][1] == "-":
                board[3][1] = botXO
                skip_action = True
                return True
            
        elif (board[2][2] == playerXO) and ((board[2][2] == board[3][1] == board[0][4])):
            if board[1][3] == "-":
                board[1][3] = botXO 
                skip_action = True
                return True

        elif (board[1][3] == playerXO) and ((board[1][3] == board[0][4] == board[3][1])):
            if board[2][2] == "-":
                board[2][2] = botXO
                skip_action = True
                return True
            
        elif (board[1][3] == playerXO) and ((board[1][3] == board[0][4] == board[3][1])):
            if board[2][2] == "-":
                board[2][2] = botXO
                skip_action = True
                return True 

        elif (board[4][1] == playerXO) and ((board[4][1] == board[2][3] == board[1][4])):
            if board[3][2] == "-":
                board[3][2] = botXO
                skip_action = True
                return True
            
        elif (board[4][1] == playerXO) and ((board[4][1] == board[3][2] == board[1][4])):
            if board[2][3] == "-":
                board[2][3] = botXO
                skip_action = True
                return True
            
        elif (board[0][3] == playerXO) and ((board[0][3] == board[1][2] == board[3][0])):
            if board[2][1] == "-":
                board[2][1] = botXO
                skip_action = True
                return True
            
        elif (board[0][3] == playerXO) and ((board[0][3] == board[2][1] == board[3][0])):
            if board[1][2] == "-":
                board[1][2] = botXO
                skip_action = True
                return True
        
    def another_diagonal_move2(board, playerXO):
        global skip_action 
            #condition for 2 in a row + 1
        if (board[0][0] == playerXO) and ((board[0][0] == board[1][1] == board[3][3])):
            if board[2][2] == "-":
                board[2][2] = botXO
                skip_action = True
                return True
            
        elif (board[1][1] == playerXO) and ((board[1][1] == board[3][3] == board[4][4])):
            if board[2][2] == "-":
                board[2][2] = botXO 
                skip_action = True
                return True 

        elif (board[1][1] == playerXO) and ((board[1][1] == board[2][2] == board[4][4])):
            if board[3][3] == "-":
                board[3][3] = botXO
                skip_action = True
                return True
            
        elif (board[0][0] == playerXO) and ((board[0][0] == board[2][2] == board[3][3])):
            if board[1][1] == "-":
                board[1][1] = botXO
                skip_action = True
                return True 

        elif (board[1][0] == playerXO) and ((board[1][0] == board[3][2] == board[4][3])):
            if board[2][1] == "-":
                board[2][1] = botXO
                skip_action = True
                return True
            
        elif (board[1][0] == playerXO) and ((board[1][0] == board[2][1] == board[4][3])):
            if board[3][2] == "-":
                board[3][2] = botXO
                skip_action = True
                return True
            
        elif (board[0][1] == playerXO) and ((board[0][1] == board[2][3] == board[3][4])):
            if board[1][2] == "-":
                board[1][2] = botXO
                skip_action = True
                return True
            
        elif (board[0][1] == playerXO) and ((board[0][1] == board[1][2] == board[3][4])):
            if board[2][3] == "-":
                board[2][3] = botXO
                skip_action = True
                return True
            
    def block_easy_win_row(board, playerXO):
        global skip_action
        for i in range(5):
            #condition for 3 in a row
            if (board[i][2] == playerXO) and ((board[i][2] == board[i][1])):
                if board[i][3] == "-":
                    board[i][3] = botXO
                    skip_action = True
                    return True
                
            elif (board[i][2] == playerXO) and ((board[i][2] == board[i][3])):
                if board[i][1] == "-":
                    board[i][1] = botXO
                    skip_action = True
                    return True
                
            elif (board[i][1] == playerXO) and ((board[i][1] == board[i][3])):
                if board[i][2] == "-":
                    board[i][2] = botXO
                    skip_action = True
                    return True            
    
    def block_easy_win_diagonal(board, playerXO):
        global skip_action 
        if (board[2][2] == playerXO) and ((board[2][2] == board[1][3])):
            if board[3][1] == "-":
                board[3][1] = botXO
                skip_action = True
                return True
                
        elif (board[2][2] == playerXO) and ((board[2][2] == board[3][1])):
            if board[1][3] == "-":
                board[1][3] = botXO
                skip_action = True
                return True

        elif (board[2][2] == playerXO) and ((board[2][2] == board[1][1])):
            if board[3][3] == "-":
                board[3][3] = botXO
                skip_action = True
                return True

        elif (board[2][2] == playerXO) and ((board[2][2] == board[3][3])):
            if board[1][1] == "-":
                board[1][1] = botXO
                skip_action = True
                return True
            
    if botXO == "O":
        for player in ['O', 'X']: #winning/block move
            if row_move(game_board,player): #check 3 in a row condition
                break
            elif row_move(board_col,player):
                break
            elif row_move2(game_board, player): #check 2 + _ + 1
                break
            elif row_move2(board_col,player):
                break
            elif diagonal_move(game_board, player): #3 in row, diagonal
                break
            elif another_diagonal_move(game_board, player):
                break
            elif diagonal_move2(game_board, player): #2 + _ + 1, diagonal
                break
            elif another_diagonal_move2(game_board, player):
                break
                
        if skip_action == False: #advantage move
            for player in ['O', 'X']:
                if block_easy_win_row(game_board, player): #block middle move
                    break
                elif block_easy_win_row(board_col, player):
                    break
                elif block_easy_win_diagonal(game_board, player):
                    break
        
        if skip_action == False:
            special_comp_move(botXO)
            
    elif botXO == "X":
        for player in ['X', 'O']: #winning/block move
            if row_move(game_board,player): #check 3 in a row condition
                break
            elif row_move(board_col,player):
                break
            elif row_move2(game_board, player): #check 2 + _ + 1
                break
            elif row_move2(board_col,player):
                break
            elif diagonal_move(game_board, player): #3 in row, diagonal
                break
            elif another_diagonal_move(game_board, player):
                break
            elif diagonal_move2(game_board, player): #2 + _ + 1, diagonal
                break
            elif another_diagonal_move2(game_board, player):
                break
                
        if skip_action == False: #advantage move
            for player in ['X', 'O']:
                if block_easy_win_row(game_board, player): #block middle move
                    break
                elif block_easy_win_row(board_col, player):
                    break
                elif block_easy_win_diagonal(game_board, player):
                    break
    
        if skip_action == False:
            special_comp_move(botXO)

def test_vs_smartAI():

    """
    A game function VS AI BOT
    Two options : Either player starts, or AI BOT
    """
    global game_over 
    global game_board
    global counter
    
    def player_moves_first():
        global game_over
        global counter
        global skip_action
        print_board(game_board)
        while game_over == False:
            player_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            smart_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)

    def comp_moves_first():
        global game_over
        global counter
        global skip_action
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            smart_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            player_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            
    player_toss = random.randint(0, 10)
    AI_toss = random.randint(0, 10)
    if player_toss > AI_toss :
        print("\n" + "player starts first" + "\n")
        player_moves_first()
    else:
        print("\n" + "BOT starts first" + "\n")
        comp_moves_first()
        

#test_vs_smartAI()

def middle_comp(botXO):
    AI_toss = random.choices(["smart","random"],(0.75,0.25))
    AI_move = str(AI_toss).strip("[]''")

    if AI_move == "smart":
        smart_comp(botXO)
    else:
        random_comp_move(botXO)

def test_vs_middle_comp():
    # global game_over 
    # global game_board
    # global counter
    
    def player_moves_first():
        global game_over
        global game_board
        global counter
        global skip_action
        print_board(game_board)
        while game_over == False:
            player_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            middle_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)

    def comp_moves_first():
        global game_over
        global game_board
        global counter
        global skip_action
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            middle_comp("O")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            skip_action = False
            player_move("X")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
        
        
        
    player_toss = random.randint(0, 10)
    AI_toss = random.randint(0, 10)
    if player_toss > AI_toss :
        print("\n" + "player starts first" + "\n")
        player_moves_first()
    else:
        print("\n" + "BOT starts first" + "\n")
        comp_moves_first()
        
#test_vs_middle_AI()

def test_game_midcomp_vs_midcomp():
    """
    A game function of regular BOT (X) vs regular BOT (O)

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    """
    global game_over 
    global game_board
    global counter
    global skip_action
    
    print_board(game_board)
    while game_over == False:
        time.sleep(2)
        skip_action = False
        middle_comp("X")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1
        if game_over:
            break
        elif counter == 25:  # condition for draw
            game_over = True
            print("Game Draw")
            break
        time.sleep(2)
        skip_action = False
        middle_comp("O")
        print("\n")
        print_board(game_board)
        counter += 1
        game_decider(game_board)
        
def test_game_smartcomp_vs_smartcomp():
    """
    A game function of Smart BOT (X) vs Smart BOT (O)

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    """
    global game_over 
    global game_board
    global counter
    global skip_action
    
    print_board(game_board)
    while game_over == False:
        time.sleep(2)
        skip_action = False
        smart_comp("X")
        print("\n")
        print_board(game_board)
        game_decider(game_board)
        counter += 1
        if game_over:
            break
        elif counter == 25:  # condition for draw
            game_over = True
            print("Game Draw")
            break
        time.sleep(2)
        skip_action = False
        smart_comp("O")
        print("\n")
        print_board(game_board)
        counter += 1
        game_decider(game_board)

def test_game_midcom_vs_smartAI(mode): #mode means who makes a move first   
    """
    A game function of Smart BOT vs Regular BOT

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    """
    global game_over 
    global game_board
    global counter
    global skip_action
    
    if mode == "smart":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            smart_comp("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            middle_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
    
    elif mode == "regular":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            middle_comp("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            smart_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
            
def test_game_midcom_vs_com(mode):
    """
    A game function of Easy BOT vs Regular BOT

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    mode = "easy" or "regular"
    mode defined which BOT will get the first turn 
    """
    global game_over 
    global game_board
    global counter
    global skip_action
    
    if mode == "easy":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            random_comp_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            middle_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
    
    elif mode == "regular":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            middle_comp("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            random_comp_move("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
 
            
def test_game_com_vs_smartAI(mode):
    """
    A game function of Easy BOT vs Smart BOT

       **Use of time.sleep twice is to give an experience of "thinking" delay by the computer.
       Also to make sure the game doesn't end in less than 5 seconds.

    mode = "easy" or "smart"
    mode defined which BOT will get the first turn 
    """
    global game_over 
    global game_board
    global counter
    global skip_action
    
    if mode == "easy":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            random_comp_move("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            smart_comp("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)
    
    elif mode == "smart":
        print_board(game_board)
        while game_over == False:
            time.sleep(2)
            skip_action = False
            smart_comp("X")
            print("\n")
            print_board(game_board)
            game_decider(game_board)
            counter += 1
            if game_over:
                break
            elif counter == 25:  # condition for draw
                game_over = True
                print("Game Draw")
                break
            time.sleep(2)
            skip_action = False
            random_comp_move("O")
            print("\n")
            print_board(game_board)
            counter += 1
            game_decider(game_board)    
    
    
    



def start_game():
    """
    Game Design:
        1) Introduction of the game modes
        2) Selection of game mode
        3) Choice to restart the game
        4) Resetting all the global variables in order for new game to restart.
    """
    
    global game_board 
    global game_over
    global counter 
    global skip_action
    time.sleep(1)
    print("Welcome to the MNK Game!")
    time.sleep(1)
    
    while True:
        game_board = np.array([["-" , "-" , "-" , "-" , "-"],
                               ["-" , "-" , "-" , "-" , "-"],
                               ["-" , "-" , "-" , "-" , "-"],
                               ["-" , "-" , "-" , "-" , "-"],
                               ["-" , "-" , "-" , "-" , "-"]])

        game_over = False
        counter = 0
        skip_action = False
        
        
        
        game_mode = input('Which mode you want to play?: ' \
                      '\n (1) Player vs Player Mode ' \
                      '\n (2) Player vs Easy COM ' \
                      '\n (3) Player vs Regular COM'
                      '\n (4) Player vs Smart COM ' \
                      '\n (5) COM vs COM ' \
                      '\n (6) Exit'\
                      '\n')

    
        if game_mode.isdigit() and int(game_mode) > 0 and int(game_mode) < 7:
            if game_mode == "1":
                test_game()
                
            elif game_mode == "2":
                test_game_vs_com()
                
            elif game_mode == "3":
                test_vs_middle_comp()
                
            elif game_mode == "4":
                test_vs_smartAI()
                
            elif game_mode == "5":
                while True:
                    first_com = input("Which COM move first?" \
                                      "\n (1) Easy COM" \
                                      "\n (2) Regular COM " \
                                      "\n (3) Smart COM " \
                                      "\n")
    
                    second_com = input("Which COM move second?" \
                                      "\n (1) Easy COM" \
                                      "\n (2) Regular COM " \
                                      "\n (3) Smart COM " \
                                      "\n (4) Exit " \
                                      "\n")
                    
                    if first_com.isdigit() and second_com.isdigit():
                        if 0 < int(first_com) <= 3 and 0 < int(second_com) <= 3:
                            if first_com == "1" and second_com == "1":
                                test_game_com_vs_com()
                                break
                            
                            elif first_com == "1" and second_com == "2":
                                test_game_midcom_vs_com("easy")
                                break
                                
                            
                            elif first_com == "1" and second_com == "3":
                                test_game_com_vs_smartAI("easy")
                                break
                            
                            elif first_com == "2" and second_com == "1":
                                test_game_midcom_vs_com("regular")
                                break
                            
                            elif first_com == "2" and second_com == "2":
                                test_game_midcomp_vs_midcomp()
                                break
                            
                            elif first_com == "2" and second_com == "3":
                                test_game_midcom_vs_smartAI("regular")
                                break
                            
                            elif first_com == "3" and second_com == "1":
                                test_game_com_vs_smartAI("smart")
                                break
                            
                            elif first_com == "3" and second_com == "2":
                                test_game_midcom_vs_smartAI("smart")
                                break
                            
                            elif first_com == "3" and second_com == "3":
                                test_game_smartcomp_vs_smartcomp()
                                break
                        
                        elif second_com == "4":
                            break
                        
                        else:
                            print("Wrong input")
                            
                    else:
                        print("Wrong input")
                            

            elif game_mode == "6":
                print("Thank you for trying our game. Have a nice day!")
                break
        else:
            print("Wrong input!")
            
        play_again = ""
        while True: 
            play_again = input("Want to play again? (y) yes or (n) no \n")
            if play_again != "y" and play_again != "n":
                print("Wrong input")
            else:
                break
                
        if play_again == "n":
            print("Thank you for trying our game. Have a nice day!")
            break
        else:
            continue
            
        
            
start_game()
     
    

