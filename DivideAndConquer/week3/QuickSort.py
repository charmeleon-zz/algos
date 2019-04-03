def quick_sort(A, left, right):
    """
    Input: array A, left and right endpoints; left and right ϵ {1, ..., n}
    Postcondition: elements of the subarray A[left], A[left + 1], ...., A[right] are sorted
    from smallest to largest
    """
    # terminating condition: length is 0 or 1
    if left >= right:
        return
    # partition A around pivot; j = new pivot position
    j = partition(A, left, right)
    # recurse on left
    quick_sort(A, left, j - 1)
    # recurse on right
    quick_sort(A, j + 1, right)

def partition(A, left, right):
    """
    Input: array A of n distinct integers, left and right boundaries
    Postcondition: elements of the subarray `A[l], A[l +1], ..., A[r] are partitioned around A[l]`
    Output: final position of pivot element
    """
    # make the first element in the array the pivot
    pivot_index = choose_pivot(A, left, right)
    pivot = A[pivot_index]
    # i marks the boundary in partitioned elements where elements are > pivot
    i = pivot_index + 1
    # __Claim__: the for loop maintains the invariant
    # A[k] < pivot for k ϵ {left + 1, ..., i - 1}
    # A[k] > pivot for k ϵ {i, ..., A[j - 1] are all greater than the
    # j marks the boundary of unpartitioned elements
    for j in range(i, right + 1):
        # TODO can avoid redundant swaps by keeping track of whether we have seen any elements bigger than the pivot
        if A[j] < pivot:
            # swap leftmost element bigger than the pivot
            swap(A, i, j)
            i += 1
    # place pivot in correct position by swapping pivot with last element less than it
    swap(A, pivot_index, i - 1)
    # report pivot's position
    return i - 1

def swap(A, m, n):
    """Swap the position of two arbitrary elements in an array"""
    A[m], A[n] = A[n], A[m]

def choose_pivot(A, left, right):
    return left
