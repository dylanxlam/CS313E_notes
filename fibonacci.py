# 2 ** n time complexity

def fib_memo(n, memo):
    if n == 0 or n == 1:
        return n
    else:
        if n >= len(memo):
            f = fib_memo(n-1, memo) + fib_memo(n-2, memo)
            memo.append(f)
            return f
        else:
            return memo[n]

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
def main():

    '''
    for i in range(50):
        print(i,' ', fib_rec(i))
    '''

    memo = [0,1]
    for i in range(50):
        print(i,' ', fib_memo(i, memo))


main()