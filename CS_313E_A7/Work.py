import sys, time

# Helper function to calculate the number of lines Vyasa can write before falling asleep
def lines_before_sleep(n: int, k: int, v: int) -> int:
    total_lines = 0
    productivity = 1

    while v > 0:
        total_lines += v
        v = v // k
        productivity *= k

    return total_lines

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    v = 0
    while True:
        lines_written = lines_before_sleep(n, k, v)
        if lines_written >= n:
            return v
        v += 1

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search(n: int, k: int) -> int:
    low, high = 0, n

    while low < high:
        v = (low + high) // 2
        lines_written = lines_before_sleep(n, k, v)

        if lines_written >= n:
            high = v
        else:
            low = v + 1

    return low

# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        result = binary_search(n, k)
        finish = time.time()

        print("Binary Search: " + str(result))
        print("Time: " + str(finish - start))
        print()

        start = time.time()
        result = linear_search(n, k)
        finish = time.time()

        print("Linear Search: " + str(result))
        print("Time: " + str(finish - start))
        print()
        print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
