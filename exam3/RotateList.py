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

    # add an item at the beginning of the list
    def insert_first(self, item):
        new_link = Link(item)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
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

        # Get the length of the linked list
        length = 0
        current = self.first
        while current:
            length += 1
            current = current.next

        # For where k is greater than the length of the linked list
        k = k % length

        if k == 0:
            # Don't rotate if k is a multiple of the length
            return

        # Find the new head and tail positions
        new_head_pos = length - k
        new_tail_pos = new_head_pos - 1

        # Find the new head and tail nodes
        new_head_node = self.first
        new_tail_node = self.first
        for i in range(new_tail_pos):
            new_tail_node = new_tail_node.next

        # Rearrange the pointers
        self.first = new_tail_node.next
        new_tail_node.next = None

        # Connect the original head to the original tail
        current = self.first
        while current.next:
            current = current.next
        current.next = new_head_node


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
