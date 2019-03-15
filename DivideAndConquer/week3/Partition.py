def partition(A, left, right):
    '''
    __Input__ array A of n distinct integers, left and right boundaries
    __Postcondition__ elements of the subarray `A[l], A[l +1], ..., A[r] are partitioned around A[l]`
    __Output__ final position of pivot element
    '''
    pivot = A[left]
    # i keeps track of the boundary between processed elements
    i = left + 1
    for j in range(left + 1, right):
        # swap elements smaller than the pivot
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    # swap the pivot element with the last element less than it
    A[left], A[i - 1] = A[i - 1], A[left]
    # report pivot's position
    return i - 1