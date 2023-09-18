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

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(text, key):
    rails = [[] for _ in range(key)]
    rail_idx = 0
    direction = 1

    for char in text:
        rails[rail_idx].append(char)
        rail_idx += direction

        if rail_idx == 0 or rail_idx == key - 1:
            direction *= -1

    encoded_text = ''.join([''.join(rail) for rail in rails])
    return encoded_text

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    fence = [[] for _ in range(key)]
    rail = 0
    direction = 1

    for char in strng:
        fence[rail].append(None)
        rail += direction

        if rail == key - 1 or rail == 0:
            direction = -direction

    index = 0
    for rail in range(key):
        for i in range(len(fence[rail])):
            fence[rail][i] = strng[index]
            index += 1

    decoded_text = ''
    rail = 0
    direction = 1

    for _ in range(len(strng)):
        decoded_text += fence[rail].pop(0)
        rail += direction

        if rail == key - 1 or rail == 0:
            direction = -direction

    return decoded_text

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(text, passphrase):
    # Encode using Vigenere Cipher
    encoded_text = ''
    passphrase = passphrase.lower()
    text = filter_string(text)

    for i, char in enumerate(text):
        shift = ord(passphrase[i % len(passphrase)]) - ord('a')
        encoded_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        encoded_text += encoded_char

    return encoded_text

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(encoded_text, passphrase):
    # Decode using Vigenere Cipher
    decoded_text = ''
    passphrase = passphrase.lower()
    encoded_text = filter_string(encoded_text)

    for i, char in enumerate(encoded_text):
        shift = ord(passphrase[i % len(passphrase)]) - ord('a')
        decoded_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        decoded_text += decoded_char

    return decoded_text

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(text):
    # Filter the input string
    filtered_text = ''
    text = text.lower()

    for char in text:
        if 'a' <= char <= 'z':
            filtered_text += char

    return filtered_text

def main():
    while True:
        try:
            # Read the plain text or encoded text
            text = input().strip()
            if not text:
                break

            # Read the key or passphrase
            key = int(input().strip())
            
            # Read the expected output (for comparison)
            expected_output = input().strip()

            # Encode and print using Rail Fence Cipher
            encoded_rail_fence = rail_fence_encode(text, key)
            print("Encoded Text (Rail Fence):", encoded_rail_fence)
            assert encoded_rail_fence == expected_output, "Rail Fence Encoding Failed"

            # Read the key or passphrase
            passphrase = input().strip()

            # Read the expected output (for comparison)
            expected_output = input().strip()

            # Encode and print using Vigenere Cipher
            encoded_vigenere = vigenere_encode(text, passphrase)
            print("Encoded Text (Vigenere):", encoded_vigenere)
            assert encoded_vigenere == expected_output, "Vigenere Encoding Failed"

            # Decode and print using Rail Fence Cipher
            decoded_rail_fence = rail_fence_decode(encoded_rail_fence, key)
            print("Decoded Text (Rail Fence):", decoded_rail_fence)
            assert decoded_rail_fence == text, "Rail Fence Decoding Failed"

            # Decode and print using Vigenere Cipher
            decoded_vigenere = vigenere_decode(encoded_vigenere, passphrase)
            print("Decoded Text (Vigenere):", decoded_vigenere)
            assert decoded_vigenere == text, "Vigenere Decoding Failed"

        except EOFError:
            break

def main():
    # Read the plain text from stdin
    plain_text = input().strip()

    # Read the key for rail fence cipher from stdin
    key_rf = int(input().strip())

    # Encrypt and print the encoded text using Rail Fence cipher
    encoded_rail_fence = rail_fence_encode(plain_text, key_rf)
    print("Rail Fence Cipher\n")
    print("Plain Text:", plain_text)
    print("Key:", key_rf)
    print("Encoded Text:", encoded_rail_fence)

    # Read the encoded text for rail fence cipher from stdin
    encoded_text_rf = input().strip()

    # Read the key for rail fence cipher from stdin
    key_rf = int(input().strip())

    # Decrypt and print the plain text using Rail Fence cipher
    decoded_rail_fence = rail_fence_decode(encoded_text_rf, key_rf)
    print("\nEncoded Text:", encoded_text_rf)
    print("Enter Key:", key_rf)
    print("Decoded Text:", decoded_rail_fence)

    # Read the plain text from stdin
    plain_text = input().strip()

    # Read the pass phrase from stdin
    pass_phrase = input().strip()

    # Encrypt and print the encoded text using Vigenere cipher
    encoded_vigenere = vigenere_encode(plain_text, pass_phrase)
    print("\nVigenere Cipher\n")
    print("Plain Text:", plain_text)
    print("Pass Phrase:", pass_phrase)
    print("Encoded Text:", encoded_vigenere)

    # Read the encoded text from stdin
    encoded_text = input().strip()

    # Read the pass phrase from stdin
    pass_phrase = input().strip()

    # Decrypt and print the plain text using Vigenere cipher
    decoded_vigenere = vigenere_decode(encoded_text, pass_phrase)
    print("\nEncoded Text:", encoded_text)
    print("Pass Phrase:", pass_phrase)
    print("Decoded Text:", decoded_vigenere)

if __name__ == "__main__":
    main()

