class ListBoard:
    def __init__(self, board):
        self.board = board  # initializes the board with a list
        self.length = len(board)  # initializes the length of the board

    # removes a number of elements from the board
    def set_item(self, index, number):
        self.board[index] = number

        # if the index would be less than 0, change it to 0
        if self.board[index] < 0:
            self.board[index] = 0

    # prints each column in the board
    def print_board(self):
        board_string = ""
        for i in range(0, self.length):
            if i == 0:
                board_string += "|" + str(self.board[i]) + "|"
            else:
                board_string += str(self.board[i]) + "|"

        print(board_string)

    # checks if the board is empty
    def check_win_state(self):
        for item in self.board:
            if item > 0:
                return False

        return True
