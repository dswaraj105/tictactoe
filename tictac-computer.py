# imports
from random import choice
from time import sleep

# data structure
board = [' ' for x in range(9)]

# player details
player_details = {
    'name': '',
    'avatar': 'O'
}


# setting player details
def get_player_details():
    print('Enter player 1 details')
    player_details['name'] = input("Enter your name : ")
    print('Your symbol is "O"')


def display(arr):
    print()
    for i in range(3):
        print(f' {arr[0 + 3 * i]} | {arr[1 + 3 * i]} | {arr[2 + 3 * i]}'.rjust(50))
        if i < 2:
            print('---|---|---'.rjust(51))
    print()


def demo_board(arr):
    print('1   2   3 '.rjust(51))
    for i in range(3):
        print(
            f'{i + 1}   {arr[0 + 3 * i]} | {arr[1 + 3 * i]} | {arr[2 + 3 * i]}'.rjust(50))
        if i < 2:
            print('  ---|---|---'.rjust(51))
        i += 1
    print()


# taking input from player
def choose_place():
    game_help = 'You can place your avatar on the basis of table\n\t\t <<::valid inputs - 1, 2, 3::>>'
    while True:
        row_input = input('Enter the row number : ')
        if '0' < row_input < '4':
            row_input = int(row_input)
            if 0 < row_input < 4:
                break
        elif row_input.lower() == 'help':
            print(game_help)
            ch_flag = input("Do you wan the index display --<<YES?NO>> ")
            if ch_flag.lower() == 'yes':
                demo_board(board)
        else:
            print('Invalid input: try again')

    while True:
        col_input = input('Enter the column number : ')
        if '0' < col_input < '4':
            col_input = int(col_input)
            if 0 < col_input < 4:
                break
        elif col_input.lower() == 'help':
            print(game_help)
        else:
            print('Invalid input: try again')

    # make the return to array number by multiplying one by 3 and adding them
    return (row_input - 1) * 3 + col_input - 1


def comp_turn():
    spaces = []
    for i, letter in enumerate(board):
        if letter == ' ':
            spaces.append(i)

    # checking for all possible winning cases
    for sym in ['X', 'O']:
        for i in spaces:
            b_copy = board[:]
            b_copy[i] = sym
            if win_check(b_copy):
                return i

    if 4 in spaces:
        return 4

    moves = []
    for i in spaces:
        if i in [0, 2, 6, 8]:
            moves.append(i)
    if len(moves) > 0:
        return choice(moves)

    return choice(spaces)


# checking if someone won returns player name who won else returns false
def win_check(arr):
    # checking row and column matches
    for i in range(3):
        # checking row matches
        if arr[0 + 3 * i] == arr[1 + 3 * i] == arr[2 + 3 * i]:
            if arr[0 + 3 * i] == 'X' or arr[0 + 3 * i] == 'O':
                return arr[0 + 3 * i]

        # checking column matches
        if arr[i + 3 * 0] == arr[i + 3 * 1] == arr[i + 3 * 2]:
            if arr[i + 3 * 0] == 'X' or arr[i + 3 * 0] == 'O':
                return arr[i]

    # checking diagonal winner
    # checking main diagonal
    if arr[0] == arr[4] == arr[8]:
        if arr[0] == 'O' or arr[0] == 'X':
            return arr[0]

    # checking sub diagonal
    if arr[2] == arr[4] == arr[6]:
        if arr[2] == 'O' or arr[2] == 'X':
            return arr[2]

    return False


def play():
    print('You can type <<::help::>> to get info on how to play')
    print(f'Lets start the game')
    demo_board(board)
    i = 0
    flag = True

    # the loop runs till the end of the game -- max "9" times
    while i < 9:
        if flag:
            print(f"Player's turn")
            user_move = choose_place()
            if board[user_move] != ' ':
                while True:
                    print("Sorry the place is occupied")
                    user_move = choose_place()
                    if board[user_move] == ' ':
                        break
            print(user_move)
            board[user_move] = 'O'
        else:
            print(f"Computer's turn")
            sleep(1)
            comp_move = comp_turn()
            board[comp_move] = 'X'

        display(board)
        result = win_check(board)
        if result:
            winner = 'player' if result == 'O' else 'Computer'
            print(f'{winner} won')
            break

        flag = not flag
        i += 1


def init():
    global board
    get_player_details()
    flag = True
    while flag:
        play()
        print('Game over')
        response = input('Do you want to play again --<<YES/NO>>')
        if response.lower() == 'no':
            flag = False
        else:
            board = [' ' for _ in range(9)]


if __name__ == '__main__':
    init()
