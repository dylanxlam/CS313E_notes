import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    # Initialize variables to keep track of the maximum boxes and the count of sets
    max_boxes = 0
    num_sets = 0

    # Create a memoization table to store previously calculated results
    memo = {}

    # Helper function to find the maximum boxes and sets recursively
    def find_max_sets(box_idx):
        nonlocal max_boxes, num_sets
        if box_idx in memo:
            return memo[box_idx]

        # Initialize the maximum number of boxes to 1 (the box itself)
        max_boxes_here = 1
        num_sets_here = 1

        for i in range(box_idx + 1, len(box_list)):
            if does_fit(box_list[box_idx], box_list[i]):
                next_max_boxes, next_num_sets = find_max_sets(i)
                total_boxes = 1 + next_max_boxes

                if total_boxes > max_boxes_here:
                    max_boxes_here = total_boxes
                    num_sets_here = next_num_sets
                elif total_boxes == max_boxes_here:
                    num_sets_here += next_num_sets

        memo[box_idx] = (max_boxes_here, num_sets_here)
        return memo[box_idx]

    # Iterate through each box to find the maximum boxes and sets
    for i in range(len(box_list)):
        max_here, sets_here = find_max_sets(i)
        if max_here > max_boxes:
            max_boxes = max_here
            num_sets = sets_here
        elif max_here == max_boxes:
            num_sets += sets_here

    return max_boxes, num_sets

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # sort the box list
    box_list.sort()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)

if __name__ == "__main__":
    main()
