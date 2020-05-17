import random
class AdjoinTheSpheres:
    def __init__(self):
        # Class list for the board; gonna need to use it for the user's loaded map
        self.connect_board = []
        self.PLAYER_ONE_SYMBOL = 'x'
        self.PLAYER_TWO_SYMBOL = 'o'
        self.dimensions = []
        self.player_one_coordinates = []
        self.player_two_coordinates = []
        self.player_two_current_move = ''
        self.player_one_current_move = ''
        self.win_condition = False
        self.player_current_move = ''
        self.have_already_won = False
        self.exit_game = False
        self.coordinates = []
        self.loading_game = ''
        self.menu_choice = 0
        self.comp_ready_to_move = False
        self.comp_row = 0
        self.comp_col = 0
        self.tie_check_count = 0
        self.save_player = ''
        self.invalid_coord = True

    def main_menu(self):
        """
        :param: Takes in user input for what type of game they wish to play in
        :return: Menu choice so the program knows which type of game to run (CPU Vs Player) or (PVP)
        """
        print("AdjoinTheSpheres Main Menu")
        print("1) New Game (2 players) ")
        print("2) New Game (1 player vs computer)")
        print("3) Exit Game")
        self.menu_choice = int(input("Choose an option from the menu: "))
        # User's menu choice
        if self.menu_choice == 1:
            self.loading_game = input("What game/map do you want to load?: ")
        # Place the loading game method in here (PvP)
        elif self.menu_choice == 2:
            self.loading_game = input("What game/map do you want to load?: ")
            self.comp_ready_to_move = True
        # Place the load game method in here (This is the one vs computer)
        elif self.menu_choice == 3:
            # Exits game
            self.exit_game = True
        while self.menu_choice < 1 or self.menu_choice > 3:
            self.menu_choice = int(input("Choose an option from the menu: "))

    # Reads game map file and converts the spaces to periods;
    def load_board(self):
        """
            :param: Takes the game file the user enters, and loads it into a grid-like format
            :return: Returns the grid and the dimensions of the board
        """
        self.connect_board = []
        with open(self.loading_game, "r") as f:
            read_game_file = f.readlines()
            for x in read_game_file:
                replaced = x.replace(' ', '.')
                done = replaced.strip()
                self.connect_board.append(list(done))
            width = int(self.connect_board[0][0])  # width/rows
            height = int(self.connect_board[0][2])  # height/columns
            self.connect_board = self.connect_board[2:]  # the board w/o other stuff
            self.dimensions.append(width)
            self.dimensions.append(height)
            for s in self.connect_board:
                print(*s)

    def player_one_move(self):
        """
            :param: Checks if the game has been won or not, and based on that it runs and checks player movements
            while updating the board
            :return: Returns either an updated board w/ player moves or exits the game
        """
        if self.have_already_won == False:
            player_turn = "x"
            self.check_moves(player_turn)
            x = self.coordinates[0]
            y = self.coordinates[1]
            self.update_board(x, y, self.PLAYER_ONE_SYMBOL)
            self.check_win_conditions()
            self.show_board()
        else:
            self.exit_game = True

    def player_two_move(self):
        """
            :param: Checks if the game has been won or not, and based on that it runs and checks player movements
            while updating the board
            :return: Returns either an updated board w/ player 2 moves or exits the game
        """
        if self.have_already_won == False:
            player_turn = "o"
            self.check_moves(player_turn)
            x = self.coordinates[0]
            y = self.coordinates[1]
            self.update_board(x, y, self.PLAYER_TWO_SYMBOL)
            self.check_win_conditions()
            self.show_board()
        else:
            self.exit_game = True

    def comp_move(self):
        """
            :param: Checks if the game has been won or not, and based on that it runs and checks CPU movements
            while updating the board
            :return: Returns either an updated board w/ the CPU moves or exits the game
        """
        if self.have_already_won == False:
            player_turn = "o"
            self.comp_row = random.randint(1, self.dimensions[0])
            self.comp_col = random.randint(1, self.dimensions[1])
            while self.connect_board[self.comp_row - 1][self.comp_col - 1] != ".":
                self.comp_row = random.randint(1, self.dimensions[0])
                self.comp_col = random.randint(1, self.dimensions[1])
            self.connect_board[self.comp_row - 1][self.comp_col - 1] = player_turn
            self.check_win_conditions()
            print("Updated CPU Board")
            self.show_board()
        else:
            self.exit_game = True

    # [2][3] represent player_two coords

    def check_moves(self, player):
        """
        :param player: Holds the current player's symbol
        :return: Returns the coordinates to update the board if they are within the conditionals/rules
        """
        self.invalid_coord = True
        x = 0
        y = 0
        while self.invalid_coord == True:
            self.tie_check()
            print("Somehow still going")
            print(self.invalid_coord)
            self.player_current_move = input(
                    "player {} What move do you want to make? \n Answer as row (vertical) column (horizontal)"
                    " or save game or load game ".format(player))
            self.save_player = player
            if self.player_current_move == "save game":
                self.save_game()
                print("Save completed")
            elif self.player_current_move == "load game":
                self.load_game()
                print("Load completed")
            else:
                self.player_current_move = self.player_current_move.strip().split()
                x = int(self.player_current_move[0]) - 1
                y = int(self.player_current_move[1]) - 1
                if x < self.dimensions[0] and y < self.dimensions[1]:
                    if self.connect_board[x][y] == '*':
                        print("That's a forbidden area")
                    elif self.connect_board[x][y] == 'x' or self.connect_board[x][y] == 'o':
                        print("There's already a symbol there")
                    else:
                        self.coordinates = [x, y]
                        invalid_coord = False
                elif x > self.dimensions[0] or y > self.dimensions[1]:
                        print("That's out of range")

    def update_board(self, x, y, symbol):
        """
        :function Updates the board as the player inputs coordinates and uses their symbol
        :param x,  the x coordinate from the user coordinates
        :param y,  the y the coordinate from the user coordinates
        """
        self.connect_board[x][y] = symbol

    def show_board(self):
        """
        Shows the board throughout the game as it progresses
        """
        for s in self.connect_board:  # Prints out the connect board in a grid-format (I can reprint while updating)
            print(*s)

    def play_game(self):
        """
        :param: Checks if the game has been won or not, and based on that it runs the while loop, continuously
        running the game until the game is either over, or the game has been saved.
        :return: Either continues the game, or closes it based on what the users choose at the main menu
        """
        while self.have_already_won == False:
            if self.menu_choice == 2:
                self.player_one_move()
                self.comp_move()
            else:
                self.player_one_move()
                self.player_two_move()

    def horizontal_win_check(self):
        """
        Checks the board for any horizontal wins
        """
        if self.have_already_won == False:
            for i in range(len(self.connect_board)):
                for j in range(len(self.connect_board[i]) - 3):
                    if self.connect_board[i][j] == "o" or self.connect_board[i][j] == "x":
                        if self.connect_board[i][j + 1] == self.connect_board[i][j] and self.connect_board[i][j + 2] == \
                                self.connect_board[i][j] and self.connect_board[i][j + 3] == self.connect_board[i][j]:
                            print("Player {} has won the game. ".format(self.connect_board[i][j]))
                            self.have_already_won = True
                            return True

    def vertical_win_check(self):
        """
            Checks the board for any vertical wins
        """
        if self.have_already_won == False:
            for i in range(len(self.connect_board) - 3):
                for j in range(len(self.connect_board[i])):
                    if self.connect_board[i][j] == "o" or self.connect_board[i][j] == "x":
                        if self.connect_board[i + 1][j] == self.connect_board[i][j] and self.connect_board[i + 2][j] == \
                                self.connect_board[i][j] and self.connect_board[i + 3][j] == self.connect_board[i][j]:
                            print("player {} has won the game".format(self.connect_board[i][j]))
                            self.have_already_won = True
                            return True

    def diag_win_check(self):
        """
        Checks the board for any diagonal wins
        """
        if self.have_already_won == False:
            for i in range(len(self.connect_board) - 3):
                for j in range(len(self.connect_board[i]) - 3):
                    if self.connect_board[i][j] == "o" or self.connect_board[i][j] == "x":
                        if self.connect_board[i + 1][j - 1] == self.connect_board[i][j] and self.connect_board[i + 2][
                            j - 2] == self.connect_board[i][j] and self.connect_board[i + 3][j - 3] == \
                                self.connect_board[i][j]:
                            print("player {} has won the game".format(self.connect_board[i][j]))
                            self.have_already_won = True
                            return True

                        if self.connect_board[i + 1][j + 1] == self.connect_board[i][j] and self.connect_board[i + 2][
                            j + 2] == self.connect_board[i][j] and self.connect_board[i + 3][j + 3] == \
                                self.connect_board[i][j]:
                            print("player {} has won the game".format(self.connect_board[i][j]))
                            self.have_already_won = True
                            self.tie_complete = True
                            return True

    def check_win_conditions(self):
        """
        Checks all win conditions
        """
        self.tie_check()
        self.vertical_win_check()
        self.horizontal_win_check()
        self.diag_win_check()

    def save_game(self):
        """
        :return: Saves the game to a new file based on user-choice
        """
        save_name = input("What name do you wish to save this game file to?: ")
        with open(save_name.lower(), "w") as f:
            rows = str(self.dimensions[0])
            columns = str(self.dimensions[1])
            dimensions = str(rows + " " + columns)
            current_player_turn = self.save_player
            f.write(dimensions + '\n')
            f.write(str(current_player_turn + '\n'))
            for i in range(len(self.connect_board)):
                new = "".join(self.connect_board[i])
                strip_it = new.strip().replace(',', "")
                f.writelines("".join(str(strip_it)) + '\n')


    def load_game(self):
        """
        :return: Loads the user-selected game file
        """
        self.loading_game = input("What game file do you want to load?: ")
        self.load_board()


    def tie_check(self):
        """
        :return: Checks for any ties in the board by determining if there's as many symbols as total area in the grid
        """
        tie_check_count = 0
        x = int(self.dimensions[0])
        y = int(self.dimensions[1])
        for i in range(len(self.connect_board)):
            for j in range(len(self.connect_board[i])):
                if self.connect_board[i][j] == "x" or self.connect_board[i][j] == "o" or self.connect_board[i][j] == "*":
                    tie_check_count += 1
        if tie_check_count == (x * y):
            print("Tie!")
            self.invalid_coord = False
            self.have_already_won = True


if __name__ == '__main__':
    is_program_over = False     # Boolean flag for allowing continuous gameplay until game is exited
    while not is_program_over:
        connect_four = AdjoinTheSpheres()
        connect_four.main_menu()
        is_program_over = connect_four.exit_game
        if not is_program_over:
            connect_four.load_board()
            connect_four.play_game()


