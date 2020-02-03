############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    """Calculates the number of possible ways to place n
    queens on an n x n chessboard.

    :param n: number of queens/size of board

    :return combinations: number of possible arrangements
    """
    # one in row x of n * one in row x of n ...
    # n ^ n
    return n ** n

def num_placements_one_per_row(n):
    """Calculates the number of possible ways to place n
    queens on an n x n chessboard with only one per row.

    :param n: number of queens/size of board

    :return permutations: number of possible arrangements
    """
    # one in row x of n * one in row x of n-1 ...
    # n!
    return math.factorial(n)

def n_queens_valid(board):
    """Checks whether a board configuration is valid
    meaning no queen can attack another queen.

    :param board: a list a[0...k] where a[i] is the row of the ith queen

    :return is_valid: true if the configuration and false otherwise 
    """
    # queens attack along column - same number
    # queens attack along rows - implicitly valid from data type
    # queens attack along diagonal - difference in row and col are same
    for i in range(len(board)):
        for other in range(i+1, len(board)):
            col_i = board[i]
            col_other = board[other]
            if col_i == col_other:
                return False
            diff_col = abs(col_i - col_other)
            diff_row = abs(i - other)
            if diff_col == diff_row:
                return False
    return True

def n_queens_solutions(n):
    """Finds and yields valid solutions of placing
    n queens on an n by n board.

    :param n: size of board/number of queens

    :return solutions: list of possible solutions in board structure
    """
    # place queens row by row

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
