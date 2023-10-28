# File: Prices.py  

# Student Name:
# Student UT EID:
# Course Name: CS 313E
# Unique Number:

import sys

# Input: prices is a list of integers
# Output: weeks is a list of integers representing the number of weeks you need to wait for
def compute_weeks(prices):
    stack = []
    weeks = [-1] * len(prices)

    for i in range(len(prices) - 1, -1, -1):
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

        if stack:
            weeks[i] = stack[-1] - i

        stack.append(i)

    return weeks


   
   
def main():
    #read the input file from stdin
    line = sys.stdin.readline().strip()
    # convert string to a list of integers
    prices = [int(v) for v in line.split()]
    weeks = compute_weeks(prices)
    weeks_str = ' '.join([str(v) for v in weeks])
    print(weeks_str)

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()

