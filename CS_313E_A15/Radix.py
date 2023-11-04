#  File: Radix.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return self.queue.pop(0)

  def is_empty (self):
    return len(self.queue) == 0

  def size (self):
    return len(self.queue)

def radix_sort(a):
    queues = [Queue() for _ in range(37)]  # 10 digits (0-9) + 26 letters (a-z) + 1 for special characters
    alpha = "0123456789abcdefghijklmnopqrstuvwxyz"

    # Create a dictionary to map each character to an index in the queues list
    char_dict = {c: i for i, c in enumerate(alpha)}

    # Determine the maximum length of strings to determine the number of passes required
    max_len = max(len(s) for s in a)

    for i in range(max_len - 1, -1, -1):  # Starting from the least significant character
        for word in a:
            if i < len(word):
                char = word[i]
            else:
                char = '0'  # Padding for shorter strings

            index = char_dict[char]
            queues[index].enqueue(word)

        a = []
        for q in queues:
            while not q.is_empty():
                a.append(q.dequeue())

    return a

def main():
    line = sys.stdin.readline().strip()
    num_words = int(line)

    word_list = []
    for _ in range(num_words):
        line = sys.stdin.readline().strip()
        word_list.append(line)

    sorted_list = radix_sort(word_list)
    print(sorted_list)




if __name__ == "__main__":
    main()
