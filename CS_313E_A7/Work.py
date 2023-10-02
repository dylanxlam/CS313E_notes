#  File: Work.py 

#  Description:  

#  Student Name:  

#  Student UT EID:  

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys, time

# FINDING V
# 


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

def min_v(n: int, k: int):
    for i in k:


def linear_search(n: int, k: int) -> int:   
    # use linear search here
    for i in range(n):


    return 0 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # use binary search here

    return 0 # placeholder

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
