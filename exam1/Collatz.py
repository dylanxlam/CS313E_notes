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
    s = 0  # Step distance
    w = 0  # Work

    n = start
    encountered_numbers = []

    while n != 1:
        if n in step_dictionary:
            # If n has been encountered before, update work and step distance
            for num in encountered_numbers:
                step_dictionary[num] = (s, w)
                s -= 1
            s += step_dictionary[n][0]
            w += step_dictionary[n][1]
            break

        encountered_numbers.append(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        s += 1
        w += 1

    # Update step distances and work for encountered numbers
    for num in encountered_numbers:
        step_dictionary[num] = (s, w)
        s -= 1

    return (s, w)

def main():
    # You shouldn't have to change anything below this line
    queries = [int(k) for k in sys.stdin.readlines()]
    for q in queries:
        actual_steps, work_steps = step_dist(q)
        print(str(actual_steps) + ' ' + str(work_steps))

if __name__ == "__main__":
    main()
