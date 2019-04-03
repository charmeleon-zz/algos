import sys


def quick_sort(A, l, r, sum):
    if l >= r:
        return
    sum.count += r - l

    p = partition(A, l, r)
    quick_sort(A, l, p - 1, sum)
    quick_sort(A, p + 1, r, sum)


def partition(A, l, r):
    mid = choose_median(A, l, r)
    swap(A, mid, l)
    p = l
    i = p + 1

    for j in range(i, r + 1):
        if A[j] < A[p]:
            swap(A, i, j)
            i += 1

    swap(A, p, i - 1)
    return i - 1


def swap(A, l, r):
    A[l], A[r] = A[r], A[l]


def choose_median(A, l, r):
    c = int((l + r) / 2)

    try:
        median = sorted([A[l], A[c], A[r]])[1]
    except IndexError as e:
        print(len(A), l, c, r)
        sys.exit(1)
    if median == A[l]:
        return l
    if median == A[c]:
        return c
    return r
