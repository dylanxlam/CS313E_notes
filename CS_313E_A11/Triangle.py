# File: Triangle.py

# Description: Program to find the greatest path sum in a triangular grid using different approaches.

# Student's Name:

# Student's UT EID:

# Partner's Name:

# Partner's UT EID:

# Course Name: CS 313E 

# Unique Number: 

# Date Created:

# Date Last Modified:

import sys
from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force(grid):
    def find_max_path(row, col):
        if row == len(grid) - 1:
            return grid[row][col]
        left = find_max_path(row + 1, col)
        right = find_max_path(row + 1, col + 1)
        return grid[row][col] + max(left, right)
    
    return find_max_path(0, 0)

# returns the greatest path sum using greedy approach
def greedy(grid):
    max_sum = grid[0][0]
    current_col = 0
    
    for row in range(1, len(grid)):
        if grid[row][current_col] > grid[row][current_col + 1]:
            max_sum += grid[row][current_col]
        else:
            max_sum += grid[row][current_col + 1]
            current_col += 1
    
    return max_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    def find_max_path(row, col):
        if row == len(grid) - 1:
            return grid[row][col]
        left = find_max_path(row + 1, col)
        right = find_max_path(row + 1, col + 1)
        return grid[row][col] + max(left, right)
    
    return find_max_path(0, 0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    n = len(grid)

    # Create a copy of the grid to store the maximum path sums
    dp = [row[:] for row in grid]

    # Start from the second-to-last row and work upwards
    for row in range(n - 2, -1, -1):
        for col in range(len(grid[row])):
            dp[row][col] += max(dp[row + 1][col], dp[row + 1][col + 1])

    return dp[0][0]





# reads the file and returns a 2-D list that represents the triangle
def read_file():
    with open("triangle.in", "r") as file:
        n = int(file.readline().strip())
        grid = []
        for i in range(n):
            row = list(map(int, file.readline().split()))
            grid.append(row)
        return grid

def main():
    # Read triangular grid from file
    grid = read_file()
  
    # Output greatest path from exhaustive search
    result = brute_force(grid)
    print("The greatest path sum through exhaustive search is", result)
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    print("The time taken for exhaustive search in seconds is", times)

    # Output greatest path from greedy approach
    result = greedy(grid)
    print("The greatest path sum through greedy search is", result)
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    print("The time taken for greedy approach in seconds is", times)

    # Output greatest path from divide-and-conquer approach
    result = divide_conquer(grid)
    print("The greatest path sum through recursive search is", result)
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    print("The time taken for recursive search in seconds is", times)

    # Output greatest path from dynamic programming 
    result = dynamic_prog(grid)
    print("The greatest path sum through dynamic programming is", result)
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    print("The time taken for dynamic programming in seconds is", times)

if __name__ == "__main__":
    main()
