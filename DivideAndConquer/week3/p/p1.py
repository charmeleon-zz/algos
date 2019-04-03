def quick_sort(A, l, r, sum):
    if l >= r:
        return
    sum.count += r - l
    p = partition(A, l, r)

    quick_sort(A, l, p - 1, sum)
    quick_sort(A, p + 1, r, sum)


def partition(A, l, r):
    p = choose_pivot(A, l, r)
    i = p + 1
    for j in range(i, r + 1):
        if A[j] < A[p]:
            swap(A, i, j)
            i += 1
    # swap pivot with last element less than it
    swap(A, p, i - 1)
    # return pivot's new position
    return i - 1


def swap(A, l, r):
    A[l], A[r] = A[r], A[l]


def choose_pivot(A, l, r):
    return l
