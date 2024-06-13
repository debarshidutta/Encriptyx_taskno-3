class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 square grid for the game
        self.current_player = 'X'  # Initialize the current player to 'X'

    # To print the current state of the tic-tac-toe board
    def print_board(self):
        for row in range(3):
            print(' | '.join(self.board[row]))  # To separate one column from another
            if row < 2:
                print('---------')  # To separate one row from another

    # To check if the game is over
    def is_game_over(self):
        # Check rows and columns
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return True
            # Check columns
            if self.board[0][row] == self.board[1][row] == self.board[2][row] != " ":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":  # left diagonal
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        # If no one has won, check for a draw
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True

    # To make a move
    def make_move(self, row, col):
        if self.board[row][col] == " ":  # If cell is already empty
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    # To play the game
    def play(self):
        # Main game loop
        while not self.is_game_over():
            self.print_board()
            if self.current_player == 'X':
                # AI's turn
                self.ai_move()
            else:
                # User's turn
                row = int(input("Enter row(0-2): "))
                col = int(input("Enter column(0-2): "))
                if not self.make_move(row, col):
                    print("Invalid move, try again.")
            if self.is_game_over():
                print("Game Over")
                # Announce the winner
                winner = 'O' if self.current_player == 'X' else 'X'
                if winner != ' ':
                    print(f"Player {winner} wins!")
                else:
                    print("It's a draw!")

    def minimax(self, depth, is_maximizing):
        if self.is_game_over():
            if self.current_player == 'X':  # Maximizing player
                return -10
            elif self.current_player == 'O':  # Minimizing player
                return 10
            else:
                return 0  # For draw

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        self.board[row][col] = 'X'
                        score = self.minimax(depth + 1, False)
                        self.board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        self.board[row][col] = 'O'
                        score = self.minimax(depth + 1, True)
                        self.board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    self.board[row][col] = 'X'
                    score = self.minimax(0, False)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        if best_move:
            self.make_move(best_move[0], best_move[1])


# Create a game instance and then start playing
game = TicTacToe()
game.play()