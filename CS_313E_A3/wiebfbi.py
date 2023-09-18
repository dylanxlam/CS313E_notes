# File: TestCipher.py

# Description: This assignment delves into the realm
# of cryptography, an ancient art of secure communication.
# It introduces two fundamental cipher types: substitution
# and transposition. The Rail Fence Cipher, a transposition
# technique, rearranges characters in a zigzag pattern for
# encryption and decryption. In parallel, it explores the
# Vigenere Cipher, a substitution method using passphrases.
# Using an input file, this program takes encrypted and
# decrypted strings and uses the previously mentioned cryptology
# methods to complete cryptology tasks.

# Student's Name: Dylan Lam

# Student's UT EID: DXl85

# Partner's Name: Alexander Romero-Barrionuevo

# Partner's UT EID: ANR3784

# Course Name: CS 313E

# Unique Number: 52605

# Date Created: 9/15/2023

# Date Last Modified: 9/15/2023

import sys

def print_plain_text(word):
    """# Input: This function takes an input 'word'.
    # Output: 'Plain Text: word' """
    print("Plain Text:", word)

def print_encoded_text(word):
    """# Input: This function takes an input 'word'.
    # Output: 'Encoded Text: word' """
    print("Encoded Text:", word)

def print_key(key):
    """# Input: This function takes an input 'key', that is an integer.
    # Output: 'Key: (integer)' """
    print("Key:", key)

def print_passphrase(word):
    """# Input: This function takes an input 'word'.
    # Output: 'Encoded Text: word' """
    print("Pass Phrase:", word)

def rail_fence_encode ( strng, key ):
    """#  Input: strng is a string of characters and key is a positive
    #         integer 2 or greater and strictly less than the length
    #         of strng
    #  Output: function returns a single string that is encoded with
    #          rail fence algorithm"""

    # Print respective input values
    print("\nRail Fence Cypher\n")
    print_plain_text(strng)
    print_key(key)

        # Initialize the rail fence structure
    fence = [[] for _ in range(key)]
    row, direction = 0, 1

    # Populate the rail fence structure
    for char in strng:
        fence[row].append(char)
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    # Read off the characters row by row to create ciphertext
    ciphertext = ''.join([''.join(row) for row in fence])

    return ciphertext

def rail_fence_decode ( strng, key ):
    """#  Input: strng is a string of characters
    #  Output: function converts all characters to lower case and then
    #          removes all digits, punctuation marks, and spaces. It
    #          returns a single string with only lower case characters"""
    print_encoded_text(strng)
    print_key(key)
        # Initialize the rail fence structure
    fence = [[] for _ in range(key)]
    row, direction = 0, 1

    # Mark the cells where characters should be placed
    for _ in strng:
        fence[row].append(None)
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    # Fill in the characters from the strng
    idx = 0
    for row in fence:
        for i in range(len(row)):
            row[i] = strng[idx]
            idx += 1

    # Read off the characters diagonally to reveal plaintext
    row, direction = 0, 1
    plaintext = []
    for _ in range(len(strng)):
        plaintext.append(fence[row].pop(0))
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    return ''.join(plaintext)

def filter_string ( strng ):
    """#  Input: p is a character in the pass phrase and s is a character
    #         in the plain text
    #  Output: function returns a single character encoded using the 
    #          Vigenere algorithm. You may not use a 2-D list """
        # Filter the input string
    filtered_text = ''
    strng = strng.lower()

    for char in strng:
        if 'a' <= char <= 'z':
            filtered_text += char

    return filtered_text

def vigenere_encode ( strng, phrase ):
    """#  Input: strng is a string of characters and phrase is a pass phrase
    #  Output: function returns a single string that is decoded with
    #          Vigenere algorithm"""
    
    # Encode using Vigenere Cipher
    encoded_text = ''
    passphrase = phrase.lower()
    strng = filter_string(strng)

    for i, char in enumerate(strng):
        shift = ord(phrase[i % len(phrase)]) - ord('a')
        encoded_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        encoded_text += encoded_char

    print("Vigenere Cipher\n")
    print_plain_text(strng)
    print_passphrase(phrase)

    return encoded_text


def vigenere_decode ( strng, phrase ):
    # Decode using Vigenere Cipher
    decoded_text = ''
    passphrase = phrase.lower()
    encoded_text = filter_string(strng)
    print_encoded_text(strng)
    print_passphrase(phrase)


    for i, char in enumerate(encoded_text):
        shift = ord(passphrase[i % len(passphrase)]) - ord('a')
        decoded_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        decoded_text += decoded_char


    return decoded_text

def main():
    # read the plain text from stdin
    text = sys.stdin.readline().strip()

    # read the key from stdin
    key = int(sys.stdin.readline().strip())

    # encrypt and print the encoded text using rail fence cipher
    encoded_rail_fence_cipher = rail_fence_encode(text, key)
    print("Encoded Text:",encoded_rail_fence_cipher, "\n")

    # read encoded text from stdin
    text = sys.stdin.readline().strip()
    
    # read the key from stdin
    key = int(sys.stdin.readline().strip())

    # decrypt and print the plain text using rail fence cipher
    decoded_rail_fence_cipher = rail_fence_decode(text, key)
    print("Decoded Text:",decoded_rail_fence_cipher, "\n")

    # read the plain text from stdin
    text = sys.stdin.readline().strip()

    # read the pass phrase from stdin
    phrase = sys.stdin.readline().strip()

    # encrypt and print the encoded text using Vigenere cipher
    encoded_vigenere_text = vigenere_encode(text, phrase)
    print("Encoded Text:",encoded_vigenere_text,"\n")

    # read the encoded text from stdin
    text = sys.stdin.readline().strip()

    # read the pass phrase from stdin
    phrase = sys.stdin.readline().strip()

    # decrypt and print the plain text using Vigenere cipher
    vigenere_decoded = vigenere_decode(text, phrase)
    print("Decoded Text:", vigenere_decoded)

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()