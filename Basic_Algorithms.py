def selection_sort (a):
    for i in range (len(a) - 1):
        # find the minimum
        min = a[i]
        minIdx = i

    for j in range (i + 1, len(a)):
        if (a[j] < min):
            min = a[j]
            minIdx = j

    # Swap the minimum element with the element at the ith place
    a[minIdx] = a[i]
    a[i] = min

def bubble_sort1 (a):
    idx = 0
    while (idx < len(a) - 1):
        jdx = len(a) - 1
        while (jdx > idx):
            if (a[jdx] < a[jdx - 1]):
                a[jdx], a[jdx - 1] = a[jdx - 1], a[jdx]
            jdx = jdx - 1
        idx = idx + 1

def bubble_sort2 (a):
    swapped = True
    idx = 0
    while ((idx < len(a) - 1) and swapped):
        jdx = len(a) - 1
        swapped = False
        while (jdx > idx):
            if (a[jdx] < a[jdx - 1]):
                a[jdx], a[jdx - 1] = a[jdx - 1], a[jdx]
                swapped = True
            jdx = jdx - 1
        idx = idx + 1


def insertion_sort1 (a):
    for i in range (1, len(a)):
        j = i
        while ((j > 0) and (a[j] < a[j - 1])):
            a[j], a[j - 1] = a[j - 1], a[j]
            j += -1

def insertion_sort2 (a):
    for i in range (1, len(a)):
        tmp = a[i]
        j = i
        while ((j > 0) and (a[j - 1] > tmp)):
            a[j] = a[j - 1]
            j += -1
        a[j] = tmp


def sequential_search (a, x):
    for i in range (len(a)):
        if (a[i] == x):
            return i
        return -1

def binary_search (a, x):
    lo = 0
    hi = len(a) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        if (x > a[mid]):
            lo = mid + 1
        elif (x < a[mid]):
            hi = mid - 1
        else:
            return mid
    return -1

def merge (a, b):
    c = []
    idxA = 0
    idxB = 0

    while ((idxA < len(a)) and (idxB < len(b))):
        if (a[idxA] < b[idxB]):
            c.append (a[idxA])
            idxA = idxA + 1
        else:
            c.append (b[idxB])
            idxB = idxB + 1

    # if a is not empty write it out 
    while (idxA < len(a)):
        c.append (a[idxA])
        idxA = idxA + 1

    # if b is not empty write it out
    while (idxB < len(b)):
        c.append (b[idxB])
        idxB = idxB + 1

    return c

def mergeSort (a, left, right):
    if (left < right):
        center = (left + right) // 2
        mergeSort (a, left, center)
        mergeSort (a, center + 1, right)
        merge_sort (a, left, center, right)

def merge_sort (a, left, center, right):
    first1 = left
    last1 = center
    first2 = center + 1
    last2 = right
    b = []

    while ((first1 <= last1) and (first2 <= last2)):
        if (a[first1] < a[first2]):
            b.append(a[first1])
            first1 = first1 + 1
        else:
            b.append(a[first2])
            first2 = first2 + 1

    while (first1 <= last1):
        b.append(a[first1])
        first1 = first1 + 1

    while (first2 <= last2):
        b.append(a[first2])
        first2 = first2 + 1

    idxA = left
    for i in range (len(b)):
        a[idxA] = b[i]
        idxA = idxA + 1


def qsort1 (a, lo, hi):
    if (lo >= hi):
        return

    pivot = a[lo]
    m = lo;
    for i in range (lo, hi + 1): 
        if (a[i] < pivot):
            m = m + 1
            a[m], a[i] = a[i], a[m]
  
    a[lo], a[m] = a[m], a[lo]

    qsort1 (a, lo, m - 1)
    qsort1 (a, m + 1, hi)

def qsort2 (a, lo, hi):
    if (lo >= hi):
        return

    left = lo
    right = hi
    pivot = a[(lo + hi) // 2]

    while (left < right):
        while (a[left] < pivot):
            left = left + 1
        while (pivot < a[right]):
            right = right - 1

    if (left <= right):
        a[left], a[right] = a[right], a[left]
        left = left + 1
        right = right - 1

    qsort2 (a, lo, right)
    qsort2 (a, left, hi)

def permute (a, lo, hi):
    if (lo == hi):
        print (a)
    else:
        for i in range (lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute (a, lo + 1, hi)
            a[i], a[lo] = a[lo], a[i]

def combine (a, b, idxA):
    if (idxA == len(a)):
        if (len(b) > 0):
            print (b)
            return
    else:
        c = b[:]
        b.append (a[idxA])
        idxA = idxA + 1
        combine (a, b, idxA)
        combine (a, c, idxA)

def main():
    print ("Test selection sort")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    selection_sort (a)
    print (a)
    print ()

    print ("Test bubble sort 1")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    bubble_sort1 (a)
    print (a)
    print ()

    print ("Test bubble sort 2")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    bubble_sort2 (a)
    print (a)
    print ()

    print ("Test insertion sort 1")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    insertion_sort1 (a)
    print (a)
    print ()

    print ("Test insertion sort 2")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    insertion_sort2 (a)
    print (a)
    print ()

    print ("Test sequential search")
    x = 3
    print (str(x) + " " + str(sequential_search (a, x)))
    x = 25
    print (str(x) + " " + str(sequential_search (a, x)))
    print ()

    print ("Test binary search")
    x = 3
    print (str(x) + " " + str(binary_search (a, x)))
    x = 25
    print (str(x) + " " + str(binary_search (a, x)))
    print ()

    print ("Test merge")
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8]
    c = merge (a, b)
    print (a)
    print (b)
    print (c)
    print ()

    print ("Test merge sort")
    a = [9, 2, 8, 1, 3, 6, 7, 5, 4]
    mergeSort (a, 0, len(a) - 1)
    print (a)
    print ()

    print ("Test quick sort")
    a = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print (a)
    qsort1 (a, 0, len(a) - 1)
    print (a)

    b = [5, 6, 4, 7, 3, 8, 2, 9, 1]
    print (b)
    qsort2 (b, 0, len(b) - 1)
    print (b)

    print ("Test permute")
    a = [1, 3, 5]
    permute (a, 0, len(a))
    print ()

    print ("Test combine")
    a = [1, 2, 3]
    b = []
    combine (a, b, 0)
    print ()

main()