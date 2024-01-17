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
        for i in range(len(s)):
            reduced_word = s[:i] + s[i + 1:]
            if is_reducible(reduced_word, hash_table, hash_memo):
                hash_memo.add(s)
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
