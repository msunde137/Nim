
class ListBoard():
    def __init__(self, board):
        self.board = board  # initializes the board with a list
        self.length = len(board)

    # removes a number of elements from the board
    def remove(self, index, number):
        self.board[index] -= number
        if self.board[index] <= 0:
            self.board[index] = 0

    def print_board(self):
        board_string = ""
        for i in range(0, self.length):
            if i == 0:
                board_string += "|" + str(self.board[i]) + "|"
            else:
                board_string += str(self.board[i]) + "|"

        return board_string

    def check_win_state(self):
        for item in self.board:
            if item > 0:
                return False

        return True
