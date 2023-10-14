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
# or False otherwise
def is_magic(a):
    # Establish magic constant
    magic_constant = sum(a[:3])

    # Check for each row
    for i in range(0, 9, 3):
        if sum(a[i:i+3]) != magic_constant:
            return False

    # Check for each column
    for i in range(3):
        if sum(a[i::3]) != magic_constant:
            return False

    # Check both main diagonals
    if a[0] + a[4] + a[8] != magic_constant:
        return False
    if a[2] + a[4] + a[6] != magic_constant:
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
    for i, row in enumerate(square):
        print(" ".join(map(str, row)))

    print()  # Add an extra newline at the end


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

    # Handle flattened 1x1, 2x2, and 3x3 arrays
    for size in range(1, 4):
        if len(nums) == size * size:
            square = reshape(nums)
            if is_magic(square):
                print_square(square)


if __name__ == "__main__":
    main()
