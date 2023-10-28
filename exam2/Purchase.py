# File: Purchase.py
# Description: Remove purchase requests to make a list of requests valid

# Student Name: 
# Student UT EID: 
# Course Name: CS 313E
# Unique Number: 52605

import sys

# Input: a string s, where each letter represents a request to purchase a particular item
# Output: s with characters removed such that there is only one request per item. The output 
# should be the alphabetically smallest string meeting these constraints
def filter_requests(s):
    last_idx = {character: -1 for character in s}

    stack = []

    for i, character in enumerate(s):
        if i < last_idx[character]:
            continue

        
        while len(stack) > 0 and stack[-1] > character and s.find(stack[-1], i) != -1:
            removed = stack.pop()

        if character not in stack:
            stack.append(character)



    output = ''.join(stack)
    return output

def main():
    request = sys.stdin.readline().strip()
    print(filter_requests(request))

if __name__ == "__main__":
    main()


