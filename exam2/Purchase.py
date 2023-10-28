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
    last_idx = {}

    stack = []

    for character in s:
        if character not in last_idx or character > last_idx[character]:
            stack.append(character)
            last_idx[character] = len(stack) - 1



    output = ''.join(stack)
    return output


def main():
    request = sys.stdin.readline().strip()
    print(filter_requests(request))

if __name__ == "__main__":
    main()


