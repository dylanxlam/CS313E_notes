import sys

# Populate a 2-D list with numbers from 1 to n2
def make_square(n):
    square = [[0] * n for _ in range(n)]
    i, j = n - 1, n // 2
    num = 1

    while num <= n ** 2:
        square[i][j] = num
        num += 1
        new_i, new_j = (i + 1) % n, (j + 1) % n

        if square[new_i][new_j] == 0:
            i, j = new_i, new_j
        else:
            i = (i - 1) % n

    return square

# Print the magic square
def print_square(magic_square):
    for row in magic_square:
        print(" ".join(map(str, row)))

# Check if the generated square is a magic square
def check_square(magic_square):
    n = len(magic_square)
    expected_sum = n * (n ** 2 + 1) // 2

    # Check rows and columns
    for i in range(n):
        if sum(magic_square[i]) != expected_sum:
            return False
        if sum(magic_square[j][i] for j in range(n)) != expected_sum:
            return False

    # Check main diagonal
    if sum(magic_square[i][i] for i in range(n)) != expected_sum:
        return False

    # Check other diagonal
    if sum(magic_square[i][n - 1 - i] for i in range(n)) != expected_sum:
        return False

    return True

# Calculate the sum of adjacent numbers for a given number n in the square
def sum_adjacent_numbers(square, n):
    if n < 1 or n > len(square) ** 2:
        return 0

    n_row, n_col = None, None

    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j] == n:
                n_row, n_col = i, j

    adjacent_sum = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= n_row + i < len(square) and 0 <= n_col + j < len(square) and (i != 0 or j != 0):
                adjacent_sum += square[n_row + i][n_col + j]

    return adjacent_sum

def main():
    n = int(input())
    numbers = [int(line.strip()) for line in sys.stdin]

    magic_square = make_square(n)
    print_square(magic_square)

    for num in numbers:
        adjacent_sum = sum_adjacent_numbers(magic_square, num)
        print(adjacent_sum)

if __name__ == "__main__":
    main()
