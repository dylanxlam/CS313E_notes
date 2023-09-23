# File: Collatz.py
# Description: Calculate step distances of Collatz sequence starting points and
#    the work required to calculate these step distances successively
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605


import sys
step_dictionary = {}

def step_dist(start):
    if start in step_dictionary:
        return step_dictionary[start]

    s = 0
    w = 0
    n = start

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        s += 1

        if n in step_dictionary:
            w += step_dictionary[n][1]

    w += s  # Add the current step distance as work

    step_dictionary[start] = (s, w)
    return (s, w)

def main():
    # You shouldn't have to change anything below this line
    queries = [int(k) for k in sys.stdin.readlines()]
    for q in queries:
        actual_steps, work_steps = step_dist(q)
        print(str(actual_steps) + ' ' + str(work_steps))

if __name__ == "__main__":
    main()
