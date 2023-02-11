# tic tac toe game
import random, sys

def main():
    board = {'top-left': ' ', 'top-mid': ' ', 'top-right': ' ', 'mid-left': ' ', 'mid-mid': ' ', 'mid-right': ' ', 'bot-left': ' ', 'bot-mid': ' ', 'bot-right': ' '}
    
    accepted_inputs = list(board.keys())
    quit_game_key = "qqq"
    user_input = ""

    while(user_input != quit_game_key):
        draw_board(board)
        print("Enter a move (top/mid/bot-left/mid/right) or qqq to quit: ")
        user_input = input()

        while(user_input not in accepted_inputs and user_input != quit_game_key):
            print(user_input + " is not a valid input")
            print("Enter a move (top/mid/bot-left/mid/right) or qqq to quit: ")
            user_input = input()
        
        if(user_input != quit_game_key):
            assign_position(user_input, board)

            #check full board here


def check_win(player, board):
    win_conditions = [
        [board['top-left'], board['top-mid'], board['top-right']],
        [board['mid-left'], board['mid-mid'], board['mid-right']],
        [board['bot-left'], board['bot-mid'], board['bot-right']],
        [board['top-left'], board['mid-left'], board['bot-left']],
        [board['top-mid'], board['mid-mid'], board['bot-mid']],
        [board['top-right'], board['mid-right'], board['bot-right']],
        [board['top-left'], board['mid-mid'], board['bot-right']],
        [board['top-right'], board['mid-mid'], board['bot-left']]
    ]
    for condition in win_conditions:
        if(all(pos == player for pos in condition)):
            return True
    return False


def assign_position(user_input, board):
    player = "X"
    computer = "O"

    # player move
    board[user_input] = player
    draw_board(board)

    if(check_win(player, board)):
        print("You have won!")
        sys.exit()

    # pc move
    print("Computer making move...")
    move, value = random.choice(list(board.items()))
    while(value == player or value == computer):
        move, value = random.choice(list(board.items()))

    board[move] = computer
    draw_board(board)
    if(check_win(computer, board)):
        print("The computer has won!")
        sys.exit()
    


def draw_board(board):
    print("-------------")
    print("| " + board['top-left'] + " | " + board['top-mid'] + " | " + board['top-right'] + " |")
    print("-------------")
    print("| " + board['mid-left'] + " | " + board['mid-mid'] + " | " + board['mid-right'] + " |")
    print("-------------")
    print("| " + board['bot-left'] + " | " + board['bot-mid'] + " | " + board['bot-right'] + " |")
    print("-------------")


main()
