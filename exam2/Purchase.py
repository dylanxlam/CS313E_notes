# File: Purchase.py
# Description: Remove purchase requests to make a list of requests valid

# Student Name: Dylan Lam
# Student UT EID: dxl85
# Course Name: CS 313E
# Unique Number: 52605

import sys

# Input: a string s, where each letter represents a request to purchase a particular item
# Output: s with characters removed such that there is only one request per item. The output 
# should be the alphabetically smallest string meeting these constraints
def filter_requests(s):
    stack = []
    last_idx = {character: -1 for character in s}

    for i, character in enumerate(s):
        while stack and character < stack[-1] and i < last_idx[stack[-1]]:
            stack.pop()

        if i > last_idx[character]:
            last_idx[character] = i
            if character not in stack:
                stack.append(character)

    return ''.join(stack)

def main():
    request = sys.stdin.readline().strip()
    print(filter_requests(request))

if __name__ == "__main__":
    main()


