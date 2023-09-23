# File: Triangle.py
# Description: A basic 2D Triangle class
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605


import sys

def is_approximate_anagram(word1, word2, k):
    char_count_diff = abs(len(word1) - len(word2))  # Added this line to keep track of character count difference
    
    character_count = {}
    for character in word1:
        character_count[character] = character_count.get(character, 0) + 1
    
    for character in word2:
        if character in character_count and character_count[character] > 0:
            character_count[character] -= 1
        else:
            k -= 1
            char_count_diff += 1  # Incremented char_count_diff when a character is different
    
    return char_count_diff <= k  # Changed the condition for returning True/False


def main():
    # read the number of test cases
    cases = int(sys.stdin.readline())
    
    # loop through cases
    for case in range(cases):
        line = sys.stdin.readline().split()
        k, word1, word2 = int(line[0]), line[1], line[2]
        
        if (is_approximate_anagram(word1, word2, k)):
            print(word2 + ' is a/an ' + str(k) + ' approximate anagram of ' + word1)
        else:
            print(word2 + ' is not a/an ' + str(k) + ' approximate anagram of ' + word1)

if __name__ == "__main__":
    main()