"""
File: proj2_test.py
Date: 4/28/20
Section: 21
Email: mathewt1@umbc.edu
Description:
    Final version of the testing script for Connect 4,
    tests the ability of conditionals and check functions
"""


import random
from proj2 import AdjoinTheSpheres
class spheresTest(AdjoinTheSpheres):
    def __init__(self):
        self.rand = ""

    def test_connect_board(self):
        """
        :param: width (width for the board)
        :param: height (height for the board)
        :param: loading_game (takes in the game file to be loaded)
        :param: dimensions (takes in the dimensions of the board and sets width and height accordingly)
        :return: connect_board (Will return the board in a 2D-List format based off x and y)
        """
        AdjoinTheSpheres.loading_game = "game_1.m"
        AdjoinTheSpheres.load_board()

        if AdjoinTheSpheres.dimensions[0] > 0:
            print("TEST PASSED")
            print(AdjoinTheSpheres.dimensions)
            return True

        AdjoinTheSpheres.loading_game = "game_2.m"
        AdjoinTheSpheres.load_board()

        if AdjoinTheSpheres.dimensions[0] > 0:
            print("TEST PASSED")
            print(AdjoinTheSpheres.dimensions)
            return True

        AdjoinTheSpheres.loading_game = "game_3.m"
        AdjoinTheSpheres.load_board()

        if AdjoinTheSpheres.dimensions[0] > 0:
            print("TEST PASSED")
            print(AdjoinTheSpheres.dimensions)
            return True

        AdjoinTheSpheres.loading_game = "game_4.m"
        AdjoinTheSpheres.load_board()

        if AdjoinTheSpheres.dimensions[0] > 0:
            print("TEST PASSED")
            print(AdjoinTheSpheres.dimensions)
            return True

        AdjoinTheSpheres.loading_game = "game_4.m"
        AdjoinTheSpheres.load_board()

        if AdjoinTheSpheres.connect_board > 0:
            print("TEST PASSED")
            print(AdjoinTheSpheres.dimensions)
            return True





    def test_player_one_position(self):
        """
        :param: player_current_move (user input for current move along the board;
        will be equal to current move and be a continuously updated
        variable and stored into an ordered pair and placed into a list)

        :return: coordinate pair that will be sent to the update_board function as a param
        """

        AdjoinTheSpheres.coordinates = [0, 1]
        AdjoinTheSpheres.play_game()
        AdjoinTheSpheres.coordinates = [1, 1]
        AdjoinTheSpheres.play_game()
        AdjoinTheSpheres.coordinates = [5, 5]
        AdjoinTheSpheres.play_game()
        AdjoinTheSpheres.coordinates = [3, 5]
        AdjoinTheSpheres.play_game()
        AdjoinTheSpheres.coordinates = [4, 5]
        AdjoinTheSpheres.play_game()

        if AdjoinTheSpheres.coordinates > 0:
            return True
        if AdjoinTheSpheres.coordinates[0] > AdjoinTheSpheres.dimensions[0]:
            return False
        elif AdjoinTheSpheres.coordinates[0] < AdjoinTheSpheres.dimensions[0]:
            return True
        if AdjoinTheSpheres.coordinates[1] > AdjoinTheSpheres.dimensions[1]:
            return False
        elif AdjoinTheSpheres.coordinates[1] < AdjoinTheSpheres.dimensions[1]:
            return True



    def test_player_two_position(self):
        """
        :param: player_current_move (user input for current move along the board;
        will be equal to current move and be a continuously updated
        variable and stored into an ordered pair and placed into a list)

        :return: coordinate pair that will be sent to the update_board method as a param
        """
        player_two_move_list = []
        player_two_x = 2
        player_two_y = 2
        place_piece_two = "yes"
        player_two_cord = (player_two_x, player_two_y)
        player_two_move_list.append(player_two_cord)
        x = 3
        y = 3

        if "x" in AdjoinTheSpheres.connect_board:
            return True
        if "o" in AdjoinTheSpheres.connect_board:
            return True
        elif " " in AdjoinTheSpheres.connect_board:
            return False
        elif "." in AdjoinTheSpheres.connect_board:
            return True



    def test_win_condition(self):
        """
        :return: Returns if a certain player has won based on the possible win conditions (checks the board)
        """
        if AdjoinTheSpheres.have_already_won == True:
            print("TEST PASSED")
            return True
        else:
            return False


    def test_valid_move(self):
        """
        :param: player_current_move - Takes in the move of the current player and then checks if its a valid move
        :return: returns if the move is valid or not (if not, tell user to re-input)
        """
        current_move_one_x = 2
        current_move_one_y = 1
        current_move_two_x = 2
        current_move_two_y = 4
        x = 3
        y = 3

        if current_move_one_x > x:
            print("Invalid move")
            return False
        elif current_move_one_x < x:
            print("Valid move")
            return True
        if current_move_one_y > y:
            print("Invalid move")
            return False
        elif current_move_one_y < y:
            print("Valid move")
            return True
        elif current_move_two_x < x:
            print("Valid move")
            return True
        elif current_move_two_x > x:
            print("Invalid move")
            return False


if __name__ == '__main__':
    test = spheresTest()
    test.test_connect_board()
    test.test_player_one_position()
    test.test_player_two_position()
    test.test_win_condition()
    test.test_valid_move()
