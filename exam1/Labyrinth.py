# File: Labyrinth.py
# Description: A basic 2D Triangle class
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605


import sys


# Input: start is a tuple, labyrinth is a 2D list,
# instructions is a dictionary mapping tuples to characters
# Output: -1 if the instructions do not solve the labyrinth, otherwise
# the number of steps the labyrinth can be solved in by following the instructions
def try_instructions(start, labyrinth, instructions):

    def is_valid_move(new_row, new_col):
        return 0 <= new_row < len(labyrinth) and 0 <= new_col < len(labyrinth[0]) and labyrinth[new_row][new_col] != 'X'

    row, col = start
    steps_taken = 0

    while labyrinth[row][col] != 'E':
        if not (0 <= row < len(labyrinth) and 0 <= col < len(labyrinth[0])):
            return -1

        current_instruction = instructions.get((row, col), None)

        if current_instruction == 'U':
            new_row, new_col = row - 1, col
        elif current_instruction == 'D':
            new_row, new_col = row + 1, col
        elif current_instruction == 'L':
            new_row, new_col = row, col - 1
        elif current_instruction == 'R':
            new_row, new_col = row, col + 1
        else:
            return -1

        if is_valid_move(new_row, new_col):
            row, col = new_row, new_col
        else:
            return -1

        steps_taken += 1

        if steps_taken > len(labyrinth) * len(labyrinth[0]):
            return -1

    return steps_taken


def main():
    # first line of input is "num_rows num_cols"
    r, c = tuple([int(c) for c in sys.stdin.readline().strip().split()])
    
    # next line is empty
    sys.stdin.readline()

    # next r rows are the labyrinth
    labyrinth = [[*sys.stdin.readline().strip()] for _ in range(r)]
    
    # next line is empty
    sys.stdin.readline()

    # next r rows are the instructions
    instr = {}
    for i in range(r):
        # generate dictionary for this row
        temp = {(i, j): c for (j, c) in enumerate(sys.stdin.readline().strip())}
        # update instructions to include this row
        instr.update(temp)
    # next line is empty
    sys.stdin.readline()
    # last line of input is "start_row start_col"
    start = tuple([int(c) for c in sys.stdin.readline().strip().split()])
    # write output
    print(try_instructions(start, labyrinth, instr))
if __name__ == "__main__":
    main()
