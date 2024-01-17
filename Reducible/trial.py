## Problem: What are some of the longest English words that remain a valid 
# English words as you remove one letter at a time from those words?
# The letters can be removed anywhere from the word one at a time but 
# you may not rearrange the remaining letters to form a valid word. Every time 
# you remove a letter the remaining letters form a valid English word. 
# Eventually you will end up with a single letter and that single letter 
# must also be a valid English word. A valid English word is one that is 
# found in the Oxford English Dictionary or the Webster's Dictionary.

# For want of a better term we will call such words reducible words. Here are two examples of reducible words:

# 1: sprite. If you remove the r you get spite. 
# Remove the e and you get spit. Remove the s and you get pit. 
# Remove the p and you get it. Remove the t and you get i or I 
# which is a valid English word.

# 2: string. Take away the r and you have sting. 
# Take away the t and you have sing. Take away the g 
# and you have sin. Take away the s and you have in. 
# Take away the n and you have i or I which is a valid 
# English word.

# So all reducible words will reduce to one of three letters - a, i, and o. 
# We will not accept any other letter as the final one letter word.
# There is no official word list in an electronic form that we can use. 
# We will use a curated word list file called words.txt. All the words are 
# in lower case and are two letters or more in length. This word list will 
# do as our input file.

# Your output will be all the words of length 10 that are reducible. 
# You will print each word in alphabetical order on a line by itself. 
# Here is your output of reducible words of length 10.



# # Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise

import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hash_word(s, size):
    hash_idx = 0
    for letter in s:
        letter_val = ord(letter) - 96
        hash_idx = (hash_idx * 26 + letter_val) % size
    return hash_idx

def step_size(s, const):
    hash_idx = 0
    for letter in s:
        letter_val = ord(letter) - 96
        hash_idx = (hash_idx * 26 + letter_val) % const
    return const - (hash_idx % const)

def insert_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    if hash_table[index] == '':
        hash_table[index] = s
    else:
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(index + step * num_steps) % len(hash_table)] != '':
            num_steps += 1
        hash_table[(index + step * num_steps) % len(hash_table)] = s

def find_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    if hash_table[index] == s:
        return True
    elif hash_table[index] != '':
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(index + step * num_steps) % len(hash_table)] != '':
            if hash_table[(index + step * num_steps) % len(hash_table)] == s:
                return True
            num_steps += 1
    return False

def is_reducible(s, hash_table, hash_memo):
    if s == '':
        return True
    elif s in hash_memo:
        return True
    elif not find_word(s, hash_table):
        return False
    else:
        small_words = [s[:i] + s[i + 1:] for i in range(len(s))]
        for word in small_words:
            if is_reducible(word, hash_table, hash_memo):
                hash_memo.add(word)
                return True
    return False

def get_longest_words(string_list):
    if not string_list:
        return []
    max_length = max(len(word) for word in string_list)
    return [word for word in string_list if len(word) == max_length]

def find_next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


def main():
    word_list = []

    for line in sys.stdin:
        word_list.append(line.strip())

    # Calculate N based on load factor
    load_factor = 0.7
    N = int(len(word_list) / load_factor)
    N = find_next_prime(N)

    hash_table = ['' for _ in range(N)]

    M = int(0.2 * len(word_list)) + 1
    M = find_next_prime(M)

    hash_memo = set()

    for word in word_list:
        insert_word(word, hash_table)

    reducible_words = [word for word in word_list if is_reducible(word, hash_table, hash_memo)]
    longest_reducible_words = get_longest_words(reducible_words)

    longest_reducible_words.sort()
    for word in longest_reducible_words:
        print(word)

if __name__ == "__main__":
    main()
