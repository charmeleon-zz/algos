# Input: NxN matrices A, B
# Output:
# Step 1: recursively compute only 7 (cleverly chosen) products
# Step 2: do the necessary (clever) additions/subtractions
# Running time: better than cubic time
def strassen_matrix_mult(A, B):
    P1 = A(F - H)
    P2 = (A + B)H
    P3 = (C+D)E
    P4 = D(G - E)
    P5 = (A + D)(E + H)
    P6 = (B - D)(G + H)
    P7 = (A - C)(E + F)

# X*Y resulting matrix can be expressed as:
# P5 + P4 - P2 + P6    P1 + P2
# P3 + P4              P1 + P5 - P3 - P7
