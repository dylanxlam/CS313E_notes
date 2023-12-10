# File: Symmetry.py
# Description: Identify symmetric and antisymmetric trees
# Student Name: Dylan Lam
# Student UT EID: dxl85
# Course Name: CS 313E
# Unique Number: 52605

import sys
from enum import Enum

# DO NOT EDIT THIS CLASS DEFINITION
class TreeNode:
    def __init__(self, data, left=None, right=None, scratch=None):
        self.data = data
        self.left = left  # left subtree
        self.right = right  # right subtree
        self.scratch = scratch  # used for any purpose

class ReturnCode(Enum):
    NO_SYMMETRY = 0
    MIRROR_SYMMETRIC = 1
    ANTI_SYMMETRIC = 2

# Helper function to check mirror symmetry
def is_mirror_symmetric(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (
        left.data == right.data
        and is_mirror_symmetric(left.left, right.right)
        and is_mirror_symmetric(left.right, right.left)
    )

# Helper function to check antisymmetry
def is_antisymmetric(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (
        left.data == right.data
        and is_antisymmetric(left.left, right.left)
        and is_antisymmetric(left.right, right.right)
    )

# Main function to find symmetry category
def find_symmetry(root):
    if is_mirror_symmetric(root.left, root.right):
        return ReturnCode.MIRROR_SYMMETRIC
    elif is_antisymmetric(root.left, root.right):
        return ReturnCode.ANTI_SYMMETRIC
    else:
        return ReturnCode.NO_SYMMETRY

def main():
    # input format: each line is self_name data left_name right_name
    # _ reserved for empty child
    # nodes are always defined before being referenced (leaf nodes first)
    # root is thus defined as the last node in the input
    name_map = {}
    input_data = sys.stdin.readlines()
    for line in input_data:
        parts = line.strip().split()
        data = int(parts[1])
        left = None if parts[2] == '_' else name_map[parts[2]]
        right = None if parts[3] == '_' else name_map[parts[3]]
        name_map[parts[0]] = TreeNode(data, left, right)
    root_name = input_data[-1].split()[0]
    print(find_symmetry(name_map[root_name]))

if __name__ == "__main__":
    main()
