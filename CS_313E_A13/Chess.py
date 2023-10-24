#  File: Chess.py

#  Description: 

#  Student's Name: Alexander Romero-Barrionuevo

#  Student's UT EID: ANR3784
 
#  Partner's Name: Dylan Lam

#  Partner's UT EID: DXL85

#  Course Name: CS 313E 

#  Unique Number: 52605

#  Date Created: 10/20/2023

#  Date Last Modified: 10/23/2023
import sys

class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)
        self.solutions = 0  # Initialize the solution count

    # Print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # Check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    #  Recursive backtracking
    def recursive_solve(self, col):
        if (col == self.n):
            # If all queens are placed, a solution is found
            self.solutions += 1  
            self.print_board()
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    self.recursive_solve(col + 1)
                    self.board[i][col] = '*'

    # If the problem has a solution, print the board
    def solve(self):
        self.recursive_solve(0)

def main():
    # Read the size of the board from the input file
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # Create a chess board
    game = Queens(n)

    # Place the queens on the board and count the solutions
    game.solve()

    # Print the number of solutions
    print("Total number of solutions:", game.solutions)

if __name__ == "__main__":
    main()
