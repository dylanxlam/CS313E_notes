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
    if not nums or tgt == 0:
        return 0

    length = len(nums)

    # Initialize a list to store the maximum sum at each position
    max_sum = [0] * length

    # Calculate the maximum sum for each position
    for i in range(length):
        max_sum[i] = max(max_sum[i - 1] if i - 1 >= 0 else 0, nums[i] + max_sum[i - tgt] if i - tgt >= 0 else 0)

    if tgt >= length:
        return sum(nums)  # Pick all elements if tgt is greater than or equal to length

    # Initialize a list to store the indices and values of the numbers
    num_indices = [(i, num) for i, num in enumerate(nums)]

    # Manually select the maximum elements without sorting
    selected_indices = [idx for idx, _ in sorted(num_indices, key=lambda x: -x[1])[:tgt]]

    # Extract the maximum elements and update the result
    result = sum(nums[i] for i in selected_indices)

    return max(result, max_sum[-1])

if __name__ == "__main__":
    input1 = sys.stdin.readline().split()
    num_list = [int(ele) for ele in input1]
    num = int(sys.stdin.readline())
    print(pop_or_dequeue(num_list, num))