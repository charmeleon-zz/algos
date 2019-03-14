import os
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
    i = j = k = 0
    result = []
    split_inversions = 0
    size_left = len(left)
    size_right = len(right)

    while i < size_left and j < size_right:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # increase split_inv by # of elements remaining in left array
            split_inversions += size_left - i
        k += 1
    # merge stragglers
    while i < size_left:
        result.append(left[i])
        k += 1
        i += 1

    while j < size_right:
        result.append(right[j])
        k += 1
        j += 1
    return result, split_inversions

def file_to_array():
    result = []
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir}/data/IntegerArray.txt", 'r') as f:
        for line in f.readlines():
            result.append(int(line))
        f.close()
    return result

if __name__ == "__main__":
    source = file_to_array()
    (_, inversions) = sort_and_count_inv(source)
    print(f"sorted {len(_)} elements, found {inversions} inversions")