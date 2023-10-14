# File: MagicSquare.py

# Description:

# Student's Name: Alexander Romero-Barrionuevo

# Student's UT EID: ANR3784

# Partner's Name: Dylan Lam

# Partner's UT EID: DXL85

# Course Name: CS 313E

# Unique Number: 52605

# Date Created: 10/13/2023

# Date Last Modified: 10/13/2023

# Input: 1-D list of integers a
# Output: returns True if this list is a magic square
# or False otherwise
def is_magic(a):
    size = int(len(a) ** 0.5)

    if size == 1:
        return True  # 1x1 is always a magic square

    # Establish magic constant
    magic_constant = size * (size**2 + 1) // 2

    # Check for each row, column, and diagonals
    # in which sums are compared to magic constant
    for row in range(0, size ** 2, size):
        if sum(a[row:row + size]) != magic_constant:
            return False
    for column in range(size):
        if sum(a[column::size]) != magic_constant:
            return False
    if sum(a[i * (size + 1)] for i in range(size)) != magic_constant:
        return False
    if sum(a[(size - 1) * (i + 1)] for i in range(size)) != magic_constant:
        return False

    # return True as all cases pass
    return True



# Input: 1-D list of integers a and an index idx
# Output: prints only those permutations that are magic
def permute(a, idx):
    if idx == 8:
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
    size = len(square)

    if size == 1:
        # Flattened square, print numbers separated by spaces
        for row in square:
            print(" ".join(map(str, row)))
    else:
        # 3x3 square, print each element on a new line with spaces
        for row in square:
            print(" ".join(map(str, row)))
        print()


# Input: 1-D list of integers a
# Output: returns a 2-D list
def reshape(a):
    size = int(len(a) ** 0.5)
    return [a[i:i+size] for i in range(0, len(a), size)]

def main():
    # create a 1-D list of numbers from 1 to 9
    nums = list(range(1, 10))

    # call permute to get all 3x3 magic squares
    permute(nums, 0)

if __name__ == "__main__":
    main()
