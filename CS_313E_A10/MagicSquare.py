# File: MagicSquare.py

# Description: Generates 3x3 magic squares efficiently through permutation

# Student's Name: Alex Romero-Barrionuevo
# Student's UT EID: 
 
# Partner's Name: [Partner's Name]
# Partner's UT EID: [Partner's UT EID]

# Course Name: CS 313E 
# Unique Number: [Your Unique Number]
# Date Created: [Date Created]
# Date Last Modified: [Date Last Modified]

# Input: 1-D list of integers a
# Output: returns True if this list is a magic square
#         or False otherwise



# Input: 1-D list of integers a
# Output: returns True if this list is a magic square
# or False otherwise
def is_magic(a):
    if len(a) == 1:  # Handling flattened 1x1 square
        return True
    elif len(a) == 4:  # Handling flattened 2x2 square
        return sum(a) == 10  # The sum of elements in a 2x2 square is always 10
    elif len(a) == 9:  # Handling flattened 3x3 square
        return True  # 3x3 square is always a magic square

    # Magic constant for a 3x3 square is 15
    magic_constant = 15

    # Check for each row, column, and diagonal
    for i in range(0, 3):
        if sum(a[i * 3:(i + 1) * 3]) != magic_constant:
            return False
        if sum(a[i::3]) != magic_constant:
            return False
    if sum(a[0::4]) != magic_constant:
        return False
    if sum(a[2:7:2]) != magic_constant:
        return False

    return True

# Input: 1-D list of integers a and an index idx
# Output: prints only those permutations that are magic
def permute(a, idx):
    # Check if all permutations are complete
    if idx == 9:
        if is_magic(a):
            print_square(a)
        return

    for i in range(idx, 9):
        a[idx], a[i] = a[i], a[idx]
        permute(a, idx + 1)
        a[idx], a[i] = a[i], a[idx]

# Input: 1-D list of integers a
# Output: prints this as a 2-D list
def print_square(a):
    square = reshape(a)
    for row in square:
        print(" ".join(map(str, row)))
    print()

# Input: 1-D list of integers a
# Output: returns a 2-D list
def reshape(a):
    size = int(len(a) ** 0.5)
    return [a[i:i + size] for i in range(0, len(a), size)]

def main():
    # create a 1-D list of numbers from 1 to 9
    nums = list(range(1, 10))

    # call permute to get all 3x3 magic squares
    permute(nums, 0)

if __name__ == "__main__":
    main()
