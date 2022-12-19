# define a list with the name board
board = [" " for x in range(10)]

# function for placing letter at appropriate place
def insert_letter(letter, position):
    # here board at the input position = the letter
    # here we don't require return as we just want to place the letter at correct position
    board[position] = letter

# function for availabilty of free space
def free_space(position):
    # return that board positionis empty free as empty string
    return board[position] == " "

# function for look of the board
def print_board(board):
    # here whichever number was in the input letter will be placed there.
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

# function for a board that is full
def full_board(board):
    # here it is > 1 since we have included zero in the list.
    if board.count(" ") > 1:
        return False
    else:
        return True

# function for checking the winner
def winner(board,letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

# function for the player's move
def player_move():
    # declaring intial values
    run = True
    # runnning the loop as long as the variable is True
    while run:
        p_move = input("Select a position for X between 1-9:")
        # try let us test the block for error (over here they are input other than number)
        try:
            # converting input into int
            p_move = int(p_move)
            # if input from 1 to 9
            if p_move > 0 and p_move < 10:
                # check if space is free
                if free_space(p_move):
                    # stop loop for computer's turn and also insert letter at position
                    run = False
                    insert_letter("X", p_move)
                # when space isn't available
                else:
                    print("Sorry, the position is already occupied.")
            # number not between 0 to 10.
            else:
                print("Please input a number between 0 to 10.")
        # except block let us handle the error (over here it is when input is not a number)
        except:
            print("Please input a number.")

# function for computer's move
def computer_move():

    # first provide a list a possible moves
    # below is list comprehension, which means something like "for each x in board"
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    # define move for computer with initial value zero
    c_move = 0

    # taking a var let that performs loop in the list
    for let in ["O", "X"]:
        # i performing a loop through possible_moves
        for i in possible_moves:
            # creating a temporary variable with the board list which contains empty string
            temp_board = board[:]
            # update the temp var at the particular position i
            temp_board[i] = let
            # now check for winner with that temp_board
            if winner(temp_board, let):
                # if yes then update the value(position) of c_move to i and return it
                c_move = i
                return c_move

    # if there is no winner (like it is first move in the game) then:

    # create a list for corner values that are open
    # intially the list is empty
    open_corners = []
    # check for all the i values in the possible_moves whether they are corner values or not
    for i in possible_moves:
        # if values of i is in corner then append those values in the above list
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    # check if list is not null
    if len(open_corners) > 0:
        c_move = select_random(open_corners)
        return c_move

    # if center position is free
    if 5 in possible_moves:
        c_move = 5
        return c_move

    # same think as open_corners for edges
    open_edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    if len(open_edges) > 0:
        c_move = select_random(open_edges)
        return c_move

# function for random selection. Here li is list since we are using different lists as input
def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    # return the list value at the index r
    return li[r]

# main function
def main():
    print("Welcome to the Tic Tac Toe!")
    print_board(board)

    # when board is not full, here we take the negation of the function
    while not(full_board(board)):
        # check if computer is the winner
        if not(winner(board, "O")):
            # if not then next step is player's move and update the board
            player_move()
            print_board(board)
        # when computer is the winner
        else:
            print("Sorry, computer wins. Better luck next time.")
            break   # this is important as we don't want loop to go on if there is a winner

        # check the same for player but here we have 2 conditions
        if not(winner(board, "X")):
            # var containing output of the function
            move = computer_move()
            if move == 0:    # means there aren't any possible position so it returned the initial value
                print(" ")
            # when we have moves left, so inserting O(computer move) at the output of computer_move function
            else:
                insert_letter("O", move)
                print("The computer placed O on the position " + str(move) + ";")
                print_board(board)
        # when the player is winner
        else:
            print("Congratulations! You've won.")
            break

    # if the board is full
    if full_board(board):
        print("It's a tie!")

while True:
    ques = input("Do you want to play again? (Y/N)")
    if ques.upper() == "Y":
        board = [" " for x in range(10)]
        print("-----------")
        main()
    else:
        break
