
#  File: Work.py 

#  Description: This code defines functions to calculate the 
#  number of lines a programmer named Vyasa can write before 
#  falling asleep, considering his decreasing productivity after 
#  each cup of coffee. It provides both linear and binary search 
#  methods to find the minimum number of lines Vyasa must write to 
#  complete a given coding assignment while maximizing his sleep.

#  Student Name: Alexander Romero-Barrionuevo

#  Student UT EID: ANR3784

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 10/2/2023

#  Date Last Modified: 10/2/2023

import sys, time

# Input: int v, the number of lines before first coffee
#        int k, the productivity factor
# Output: The number of lines before falling asleep
def lines_before_asleep(v,k):
    lines_written = 0

    # Establish while loop to find lines written
    while v > 0:
       lines_written += v
       v //= k

    return lines_written

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # Establish varaible v (lines before coffee)
    v = 1

    # Run through linear search algorithm
    while lines_before_asleep(v, k) < n:
        v += 1

    return v


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # Establish pointers and v (lines before coffee)
    left, right = 1, n
    v = 0

    # Create binary search algorithm
    while left <= right:
        mid = left + (right - left) // 2
        lines_written = lines_before_asleep(mid, k)

        if lines_written >= n:
            v = mid
            right = mid - 1
        else:
            left = mid + 1

    return v


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()