# Thomas Selwyn
# 04-Dec-2021

answers = [0, 0]
bingo_moves = []
bingo_boards = []
boards_won = []

# Read data input
with open('data/day_4.txt') as data_file:
    read_lines = data_file.readlines()
    data_file.close()

    counter = 0
    temp_board = []
    for current in read_lines:
        counter += 1

        if counter == 1:
            bingo_moves = current.strip().split(",")
        elif counter > 2 and current.strip() != "":
            temp_board.append(current.strip().replace("  ", " ").split(" "))
        elif counter > 2 and current.strip() == "":
            bingo_boards.append(temp_board)
            temp_board = []


def playBoardWithMove(active_board, bingoCall):
    played_numbers = bingo_moves[:bingoCall]

    for x in range(5):
        for y in range(5):
            if bingo_boards[active_board][x][y] in played_numbers:
                bingo_boards[active_board][x][y] = 'x'


def hasBoardWon(active_board):
    return True if checkHorizontalVertical(active_board) else False


def checkDiagonal(active_board):
    # Diagonal (Top Left to Bottom Right)
    for x in range(5):
        if bingo_boards[active_board][x][x] != 'x':
            return False
    return True


def checkAntiDiagonal(active_board):
    # Anti Diagonal (Bottom Left to Top Right)
    for x in range(5):
        if bingo_boards[active_board][len(active_board) - 1 - x][x] != 'x':
            return False
    return True


def checkHorizontalVertical(active_board):
    for x in range(5):
        counter = [0, 0]
        for y in range(5):
            if bingo_boards[active_board][x][y] == 'x':
                counter[0] += 1
            if bingo_boards[active_board][y][x] == 'x':
                counter[1] += 1

            if counter[0] == 5 or counter[1] == 5:
                return True
    return False


def score(winning_board, last_bingo_call):
    sum = 0
    for x in range(5):
        for y in range(5):
            if bingo_boards[winning_board][x][y] != 'x':
                sum += int(bingo_boards[winning_board][x][y])
    return sum * last_bingo_call


def playGame():
    global answers

    for bingo_move_index in range(1, len(bingo_moves)):
        for board in range(len(bingo_boards)):
            if board not in boards_won:
                playBoardWithMove(board, bingo_move_index)
                if hasBoardWon(board):
                    print(
                        f"Board {board} won, on move {bingo_move_index - 1} using a {bingo_moves[bingo_move_index - 1]}")

                    boards_won.append(board)
                    if len(boards_won) == 1:
                        answers[0] = score(board, int(bingo_moves[bingo_move_index - 1]))
                    elif len(boards_won) == 99:
                        answers[1] = score(board, int(bingo_moves[bingo_move_index - 1]))


playGame()

print("***" * 15)
print(f"Final answer for Part One is {answers[0]}")
print(f"Final answer for Part Two is {answers[1]}")
print("***" * 15)
