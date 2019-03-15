'''
QuickSort
Input: array A, left and right endpoints; left and right ϵ {1, ..., n}
Postcondition: elements of the subarray A[left], A[left + 1], ...., A[right] are sorted
from smallest to largest
'''
def quick_sort(A, left, right):
    # terminating condition: length is 0 or 1
    if left >= right:
        return
    i = choose_pivot(A, left, right)
    # make pivot first: swap A[l] and A[i]
    A[left], A[i] = A[i], A[left]
    # j = new pivot position
    j = partition(A, left, right)
    # recurse on left
    quick_sort(A, left, j - 1)
    # recurse on right
    quick_sort(A, j + 1, right)