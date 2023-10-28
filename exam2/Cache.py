# File: Cache.py
# Description: Implement a cache with hash table and linked list
# Student Name: Dylan Lam
# Student UT EID: dxl 85
# Course Name: CS 313E
# Unique Number: 52605

import sys

# A class to represent a LinkedList node
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# A class to represent a LinkedList node
class LinkedList:
    def __init__(self):
        self.first = None

    # we want to always an item at the front of the linked list
    def insert_first(self, data):
        node = Node(data)
        node.next = self.first
        self.first = node

# A hash table mimicking a cache
class HashingCache:
    def __init__(self, size):
        self.con = [LinkedList() for i in range(size)]

    # Return the size of the hash table
    def size(self):
        return len(self.con)

    # Return the hash index given a number to be hashed
    # DO NOT MODIFY THIS HASH FUNCTION
    def hash_idx(self, num):
        return num % len(self.con)

########### TO DO

    # Input: a number to be hashed. Place this item in the table
    # at the desired place
    # Output: n/a
    # Place the item in the table at the desired place
    def hash(self, num):
        idx = self.hash_idx(num)
        self.con[idx].insert_first(num)


    # Input: a number to be found in the cache. If the number is
    # in cache, bring it to the front of the linked list at its index.
    # Output: the node found, or None if it is not in cache
    # Find a number in the cache and bring it to the front of the linked list at its index
    def find(self, num):
        idx = self.hash_idx(num)
        linked_list = self.con[idx]
        current = linked_list.first
        previous = None

        while current is not None:
            if current.data == num:
                if previous is not None:
                    previous.next = current.next
                    linked_list.insert_first(num)
                return current
            
            previous = current
            current = current.next

        return None


########### TO DO


    # Helper function to print out the hash table
    # DO NOT MODIFY THIS FUNCTION
    def __str__(self):
        res = '['
        for i in range(self.size() - 1):
            if self.con[i].first is None:
                res += 'None, '
            else:
                curr = self.con[i].first
                while curr is not None and curr.next is not None:
                    res += str(curr.data) + '->'
                    curr = curr.next
                if curr is not None:
                    res += str(curr.data) + ', '
        # print last item
        if self.con[-1].first is None:
            res += 'None'
        else:
            curr = self.con[-1].first
            while curr is not None and curr.next is not None:
                res += str(curr.data) + '->'
                curr = curr.next
            if curr is not None:
                res += str(curr.data)
        res += ']'
        return res

def main():
    size = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    cache = HashingCache(size)

    for i in range(n):
        cache.hash(int(sys.stdin.readline()))
    print(cache)

    m = int(sys.stdin.readline())
    for i in range(m):
        cache.find(int(sys.stdin.readline()))

    print(cache)

if __name__ == "__main__":
    main()
