# imports

# the data structure
data_arr = [['', '', ''], ['', '', ''], ['', '', '']]

# player details
player_one = {
    'name': '',
    'avatar': 'O'
}
player_two = {
    'name': '',
    'avatar': 'X'
}


# setting player details
def get_player_details():
    print('Enter player 1 details')
    player_one['name'] = input("Enter your name : ")
    print('Your symbol is "O"')
    print('Enter player 2 details')
    player_two['name'] = input("Enter your name : ")
    print('Your symbol is "x"')


# displaying the board
def display(m_arr):
    i = 0
    print()
    for arr in m_arr:
        print(f' {arr[0] if arr[0] else " "} | {arr[1] if arr[1] else " "} | {arr[2] if arr[2] else " "}'.rjust(50))
        if i < 2:
            print('---|---|---'.rjust(51))
        i += 1
    print()


# printing the demo board
def demo_board(m_arr):
    i = 0
    print('1   2   3 '.rjust(51))
    for arr in m_arr:
        print(
            f'{i + 1}   {arr[0] if arr[0] else " "} | {arr[1] if arr[1] else " "} | {arr[2] if arr[2] else " "}'.rjust(
                50))
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
                demo_board(data_arr)
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
    return [row_input - 1, col_input - 1]


# checking if someone won returns player name who won else returns false
def win_check(m_arr):
    # checking for row and column matches
    for i in range(3):
        # checking row matches
        if m_arr[i][0] == m_arr[i][1] == m_arr[i][2]:
            # print(f' won  {m_arr[i][0]}')
            return m_arr[i][0]

        # checking column matches
        if m_arr[0][i] == m_arr[1][i] == m_arr[2][i]:
            # print(f' col win {m_arr[0][i]}')
            return m_arr[0][i]

    # checking for diagonal winner
    if m_arr[0][0] == m_arr[1][1] == m_arr[2][2]:
        return m_arr[0][0]

    if m_arr[0][2] == m_arr[1][1] == m_arr[2][0]:
        return m_arr[1][1]

    return False


# playing the game
def play():
    p1 = player_one['name']
    p2 = player_two['name']
    print('You can type <<::help::>> to get info on how to play')
    print(f'Lets start the game')
    demo_board(data_arr)
    i = 0
    flag = True

    # the loop runs till the end of the game -- max "9" times
    while i < 9:
        if flag:
            print(f"{p1}'s turn")
        else:
            print(f"{p2}'s turn")
        row, col = choose_place()
        # print(f'{row} - x,  {col} - y')
        if data_arr[row][col] != '':
            while True:
                print("The position is not empty :: Choose different one")
                row, col = choose_place()
                print(row, col)
                if data_arr[row][col] == '':
                    break
        data_arr[row][col] = 'O' if flag else 'X'
        display(data_arr)
        result = win_check(data_arr)
        if result:
            winner = player_one['name'] if result == 'O' else player_two['name']
            print(f'{winner} won')
            break

        flag = not flag
        i += 1


# game starts here
def start_game():
    print('Its a two player Ti tac game')
    play()
    print("game over")
    return


# initializing the app with all the required functions
def init():
    print('Enter Players details')
    get_player_details()
    while True:
        start_game()
        flag = input("Do you want to play again <<yes/no>>")
        if flag.lower() == 'yes':
            for arr in data_arr:
                for item in arr:
                    i = ''
        else:
            break


if __name__ == '__main__':
    init()
