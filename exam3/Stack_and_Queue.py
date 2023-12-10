#######################################################################################
#######################################################################################
# Please do not grade this one
# Please grade Q1, Q3, and Q5 if possible:)
#######################################################################################
#######################################################################################


import sys

def pop_or_dequeue(nums, tgt):
    '''
    Maximize the sum by picking elements from nums

    Args:
    - nums: list of positive integers
    - tgt: a positive integer indicating how many numbers there should be.

    Returns:
    - returns the maximum sum possible of the numbers picked by the rules
    '''
    def recursive_helper(index, remaining_tgt):
        if index < 0 or remaining_tgt == 0:
            return 0

        pick_from_end = nums[index] + recursive_helper(index - 1, remaining_tgt - 1)
        dequeue_from_front = recursive_helper(index - 1, remaining_tgt)

        return max(pick_from_end, dequeue_from_front)

    return recursive_helper(len(nums) - 1, tgt)

if __name__ == "__main__":
    input1 = sys.stdin.readline().split()
    num_list = [int(ele) for ele in input1]
    num = int(sys.stdin.readline())
    print(pop_or_dequeue(num_list, num))
