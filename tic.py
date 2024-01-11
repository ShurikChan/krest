def create_board():
    board = [' '] * 9
    return board

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])

def make_move(board, position, marker):
    if board[position] == ' ':
        board[position] = marker
    else:
        print("Неверный ход, клетка занята")
        return False
    return True

def check_winner(board, marker):
    if board[0] == board[1] == board[2] == marker:
        return True
    if board[3] == board[4] == board[5] == marker:
        return True
    if board[6] == board[7] == board[8] == marker:
        return True
    if board[0] == board[4] == board[8] == marker:
        return True
    if board[2] == board[6] == board[6] == marker:
        return True
    if board[0] == board[3] == board[6] == marker:
        return True
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    return False

def check_input(position):
    if position in range(0, 10):
        return True
    print("неверное число")
    return False

def launch():
    board = create_board()
    marker = 'X'
    print_board(board)

    while True:
        print(f'Ход игрока {marker}')
        position = int(input())
        if check_input(position):
            position = position - 1
            if make_move(board, position, marker):
                print_board(board)
                if check_winner(board, marker):
                    print(f"Игрок {marker} победил!")
                    break
                marker = 'O' if marker == 'X' else 'X'
            else:
                continue

launch()
