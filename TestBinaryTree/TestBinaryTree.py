
#  File: TestBinaryTree.py

#  Description: This Python code defines a linked list-based representation of polynomials, 
        #  with functionalities to insert terms in descending order of exponents, 
        #  perform polynomial addition, multiplication, and output the results.

#  Student Name: Alexander Romero-Barrionuevo

#  Student UT EID: ANR3784

#  Partner Name:  Dylan Lam

#  Partner UT EID: DXL85

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 11/14/23

#  Date Last Modified: 11/17/23

import sys

class Node(object):
    '''
    Node class for a binary search tree.

    Attributes:
    - data: The key value of the node.
    - lChild: Reference to the left child node.
    - rChild: Reference to the right child node.
    '''
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree(object):
    '''
    Binary search tree class.

    Attributes:
    - root: Reference to the root node of the tree.
    '''
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
        Insert a node with a given key into the binary search tree.

        Parameters:
        - data: The key value to be inserted.
        '''
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        '''
        Helper method to recursively insert a node into the binary search tree.

        Parameters:
        - root: The current root node.
        - data: The key value to be inserted.

        Returns:
        - The updated root node.
        '''
        if root is None:
            return Node(data)
        if data < root.data:
            root.lChild = self._insert(root.lChild, data)
        else:
            root.rChild = self._insert(root.rChild, data)
        return root


    def is_similar(self, pNode):
        '''
        Check if two binary trees are similar.

        Parameters:
        - pNode: Another binary search tree to compare.

        Returns:
        - True if the trees are similar, False otherwise.
        '''
        return self._is_similar(self.root, pNode.root)

    def _is_similar(self, root1, root2):
        '''
        Helper method to recursively check if two binary trees are similar.

        Parameters:
        - root1: Root of the first tree.
        - root2: Root of the second tree.

        Returns:
        - True if the trees are similar, False otherwise.
        '''
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            return (
                root1.data == root2.data and
                self._is_similar(root1.lChild, root2.lChild) and
                self._is_similar(root1.rChild, root2.rChild)
            )
        return False







    def get_level(self, level):
        '''
        Get nodes at a given level from left to right.

        Parameters:
        - level: The level of the tree.

        Returns:
        - List of Node objects at the specified level.
        '''
        nodes = []
        self._get_level(self.root, level, nodes)
        return nodes  # Return the list of Node objects

    def _get_level(self, root, level, nodes):
        '''
        Helper method to recursively get nodes at a given level.

        Parameters:
        - root: Root of the tree.
        - level: The level of the tree.
        - nodes: List to store node objects.

        Returns:
        - None
        '''
        if root is None:
            return
        if level == 0:
            nodes.append(root.data)
        elif level > 0:
            self._get_level(root.lChild, level - 1, nodes)
            self._get_level(root.rChild, level - 1, nodes)





    def get_height(self):
        '''
        Get the height of the binary search tree.

        Returns:
        - The height of the tree.
        '''
        return self._get_height(self.root)

    def _get_height(self, root):
        '''
        Helper method to recursively get the height of the binary search tree.

        Parameters:
        - root: The current root node.

        Returns:
        - The height of the tree.
        '''
        if root is None:
            return 0
        left_height = self._get_height(root.lChild)
        right_height = self._get_height(root.rChild)
        return max(left_height, right_height) + 1

    def num_nodes(self):
        '''
        Get the total number of nodes in the binary search tree.

        Returns:
        - The total number of nodes.
        '''
        return self._num_nodes(self.root)

    def _num_nodes(self, root):
        '''
        Helper method to recursively get the total number of nodes.

        Parameters:
        - root: The current root node.

        Returns:
        - The total number of nodes.
        '''
        if root is None:
            return 0
        return 1 + self._num_nodes(root.lChild) + self._num_nodes(root.rChild)

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))

    # Test method is_similar()
    tree1 = Tree()
    tree2 = Tree()
    tree3 = Tree()

    for value in tree1_input:
        tree1.insert(value)

    for value in tree2_input:
        tree2.insert(value)

    for value in tree3_input:
        tree3.insert(value)

    print("Tree1 is similar to Tree2:", tree1.is_similar(tree2)) 
    print("Tree1 is similar to Tree3:", tree1.is_similar(tree3))  

    # Print the different levels of two of the trees that are different
    print("Level 2 of Tree1:", tree1.get_level(2))
    print("Level 3 of Tree2:", tree2.get_level(3))

    # Get the height of the two trees that are different
    print("Height of Tree1:", tree1.get_height())
    print("Height of Tree2:", tree2.get_height())

    # Get the total number of nodes in a binary search tree
    print("Number of nodes in Tree3:", tree3.num_nodes())

if __name__ == "__main__":
    main()
