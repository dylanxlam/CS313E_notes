import sys

# Input: 2 strings, s1 and s2, which both have length >= 0
# Output: the number of possible new strings that can be formed by merging s1 and s2
def stringMerge(s1, s2):
    # Helper function to count the number of possible merges
    def count_merges(i, j):
        # Base cases: if either string is empty, there's only one possible merge
        if i == len(s1) or j == len(s2):
            return 1
        
        # Check if the characters at the current position in both strings are the same
        if s1[i] == s2[j]:
            # If the characters are the same, we have two options:
            # 1. Merge them and move both pointers
            # 2. Skip one character from either string
            return count_merges(i + 1, j + 1) + count_merges(i + 1, j)
        else:
            # If the characters are different, we can only move one pointer
            return count_merges(i + 1, j)
    
    return count_merges(0, 0)

def main():
    # read in 2 input strings
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    # find all new strings
    result = stringMerge(s1, s2)
    print(result)

if __name__ == '__main__':
    main()
