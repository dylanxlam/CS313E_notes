# File: StringMerge.py
# Description: Determine how many new strings can be formed according to the criteria given using recursion.
# Student Name:
# Student UT EID:
# Course Name: CS 313E
# Unique Number:

import sys

# Input: 2 strings, s1 and s2, which both have length >= 0
# Output: the number of possible new strings that can be formed by merging s1 and s2
def stringMerge(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 1
    
    count = 0

    if len(s1) > 0:
        count = count + stringMerge(s1[1:], s2)

    if len(s2) > 0:
        count = count + stringMerge(s1, s2[1:])

    return count

def main():
    # read in 2 input strings
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    # find all new strings
    result = stringMerge(s1, s2)
    print(result)

if __name__ == '__main__':
    main()
