import sys

def is_prime(n):
    if n <= 1:
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
    return const - (hash_word(s, const))

def insert_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    step = step_size(s, 13)  # Random prime for double hashing
    while hash_table[idx] != '':
        idx = (idx + step) % len(hash_table)
    hash_table[idx] = s

def find_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    step = step_size(s, 13)  # Random prime for double hashing
    while hash_table[idx] != '':
        if hash_table[idx] == s:
            return True
        idx = (idx + step) % len(hash_table)
    return False

def is_reducible(s, hash_table, hash_memo):
    counter = 0
    for i in range(len(s)):
        if counter < 10:  # Adjust the limit as needed
            print(f"Checking reducibility for: {s}")  # Debug print statement
            counter += 1
        if s in hash_memo:
            return True
        if len(s) == 1:
            return True
        sub_word = s[:i] + s[i + 1:]
        if counter < 10:  # Limit sub_word debug prints
            print(f"Checking sub_word: {sub_word}")  # Debug print statement
        if find_word(sub_word, hash_table) and is_reducible(sub_word, hash_table, hash_memo):
            hash_memo.add(sub_word)
            return True
    return False



def get_longest_words(string_list, hash_table, hash_memo):
    reducible_words = [word for word in string_list if is_reducible(word, hash_table, hash_memo)]
    
    reducible_words.sort(key=len, reverse=True)
    
    max_length = len(reducible_words[0]) if reducible_words else 0
    longest_words = [word for word in reducible_words if len(word) == max_length]

    return longest_words



def find_next_prime(n):
    while not is_prime(n):
        n += 1
    return n

def main():
    word_list = []

    for line in sys.stdin:
        word_list.append(line.strip())

    N = 200000  # Define a suitable prime number for hash table size

    hash_table = ['' for _ in range(N)]

    for word in word_list:
        insert_word(word, hash_table)

    M = 30000  # Define another prime number for memoization table size
    hash_memo = set()

    reducible_words = []
    for word in word_list:
        if is_reducible(word, hash_table, hash_memo):
            reducible_words.append(word)

    longest_words = get_longest_words(reducible_words, hash_table, hash_memo)
    for word in sorted(longest_words):
        print(word)


if __name__ == "__main__":
    main()
