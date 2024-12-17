from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def check_victory(board, sign):
    for row in range(3):
        if all([board[row][col] == sign for col in range(3)]):  
            return True
    for col in range(3):
        if all([board[row][col] == sign for row in range(3)]):  
            return True
    if all([board[i][i] == sign for i in range(3)]) or all([board[i][2-i] == sign for i in range(3)]): 
        return True
    return False


def computer_move(board):
    free = make_list_of_free_fields(board)
    move = randrange(len(free))
    row, col = free[move]
    board[row][col] = 'X'


def check_tie(board):
    free = make_list_of_free_fields(board)
    return len(free) == 0


def play_game():
    
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]  
    display_board(board)
    
    while True:
        
        while True:
            move = input("Enter your move: ")
            if move in [str(num) for num in range(1, 10)]:
                row, col = divmod(int(move)-1, 3)
                if board[row][col] not in ['O', 'X']:
                    board[row][col] = 'O'
                    break
            print("Invalid move. Try again.")
        
        display_board(board)
        
        if check_victory(board, 'O'):
            print("You won!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        
        
        print("Computer's move:")
        computer_move(board)
        display_board(board)
        
        if check_victory(board, 'X'):
            print("The computer won!")
            break
        if check_tie(board):
            print("It's a tie!")
            break


play_game()
