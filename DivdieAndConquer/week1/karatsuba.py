def karatsuba(num, num2):
    if num < 10 or num2 < 10:
        return num * num2
    # calculate the length of the numbers
    n = min(int_size(num), int_size(num2))
    m = int(n/2)
    splitter = 10**m
    # split num
    a = num // splitter
    b = num % splitter
    # split num2
    c = num2 // splitter
    d = num2 % splitter
    # karatsuba seems to fail when n is odd -- WHY
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(b + a, d + c)
    # nospace
    return (ac * (10 ** n)) + ((pq - ac - bd)*(10**m)) + bd

def int_size(num):
    return len(str(num))
