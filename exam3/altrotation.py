class Link:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # linked list class
    # feel free to add helper methods but do not change existing methods

    # create a linked list
    def __init__(self):
        self.first = None

    # add at the beginning of the list
    def insert_first(self, item):
        new_link = Link(item)

        new_link.next = self.first
        self.first = new_link

    # add at the end of a list
    def insert_last(self, item):
        new_link = Link(item)

        current = self.first
        if current is None:
            self.first = new_link
            return
        while current.next is not None:
            current = current.next
        current.next = new_link

    def rotate(self, k):
        # rotates self by k spaces
        assert k > 0

        # Find the length of the linked list
        current = self.first
        length = 0
        while current is not None:
            length += 1
            current = current.next

        # Where the linked list is empty or k is larger than the length
        if length == 0 or k % length == 0:
            return  # No rotation needed

        # Find the new last node after rotation
        new_last = self.first
        for _ in range(length - k % length - 1):
            new_last = new_last.next

        # Update pointers to perform rotation
        new_first = new_last.next
        new_last.next = None
        current = new_first
        while current.next is not None:
            current = current.next
        current.next = self.first
        self.first = new_first


if __name__ == "__main__":
    # write debug statements, test cases, etc (use assert statements)
    # this code will not be run on the autograder, only rotate will be tested
    linked_list = LinkedList()
    for i in range(1, 6):
        linked_list.insert_last(i)

    linked_list.rotate(2)

    # After rotation, the linked list should be 4 -> 5 -> 1 -> 2 -> 3
    current = linked_list.first
    expected_values = [4, 5, 1, 2, 3]

    for value in expected_values:
        assert current is not None and current.data == value
        current = current.next

    print("Rotation test passed!")