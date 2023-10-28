#  File: Div13.py

#  Description: This function return the square of the number of steps to make an inputted number (n) divisible by 13, or -1 if it is impossible

#  Student Name: Dylan Lam

#  Student UT EID: dxl85

#  Course Name: CS 313E

#  Unique Number: 52605


import sys

def is_divisible_by_13(num):
    return num % 13 == 0

# Input: n is an integer
# Output: return the square of the number of steps to make n divisible by 13, or -1 if it is impossible 
def div(n):
    memo = {}

    def min_steps(current_num):
        if is_divisible_by_13(current_num):
            return 0
        if current_num == 0:
            return 0
        if current_num in memo:
            return memo[current_num]


        str_num = str(current_num)
        min_step_count = float('inf')

        for i in range(len(str_num)):
            if (i == 0 and str_num[i] == '0' and len(str_num) > 1) or len(str_num[:i] + str_num[i + 1:]) == 0:
                continue ######### Skip lines if conditinos are met
            new_num = int(str_num[:i] + str_num[i + 1:])
            steps = 1 + min_steps(new_num)
            min_step_count = min(min_step_count, steps)

        memo[current_num] = min_step_count
        return min_step_count

    result = min_steps(n)
    return result * result if result != float('inf') else -1


def main():
    print(div(int(sys.stdin.readline())))


if __name__ == "__main__":
    main()