# Input: array A of n distinct integers
# Output: (sorted array B with the same integers, number of inversions in A)
def sort_and_count_inv(array):
    size = len(array)
    # base case
    if size == 0 or size == 1:
        return (array, 0)
    half = size // 2
    (C, left_inversions) = sort_and_count_inv(array[:half])
    (D, right_inversions) = sort_and_count_inv(array[half:])
    (B, split_inversions) = merge_and_count_split_inversions(C, D)
    return B, split_inversions + left_inversions + right_inversions

# Input: sorted arrays left and right (size n/2 each)
# Output: sorted array (length n) and number of split inversions
def merge_and_count_split_inversions(left, right):
    i = j = 0
    result = []
    split_inversions = 0
    half_n = len(left)
    for k in range(0, half_n * 2 - 1):
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
            # split inversions increment by # of elements left in left
            split_inversions += half_n - i
    return result, split_inversions