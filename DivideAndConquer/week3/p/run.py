import os

from p1 import quick_sort as q1
from p2 import quick_sort as q2
from p3 import quick_sort as q3

class Counter:
    def __init__(self):
        self.count = 0

def get_data():
    d = os.path.dirname(os.path.realpath('../data'))
    A = []
    size = 0
    with open(f"{d}/data/QuickSort.txt", 'r') as f:
        for line in f.readlines():
            size += 1
            A.append(int(line))
        f.close()
    return (A, size)

if __name__ == '__main__':
    s1 = Counter()
    s2 = Counter()
    s3 = Counter()
    (d1, size) = get_data()
    (d2, _) = get_data()
    (d3, _) = get_data()
    q1(d1, 0, size - 1, s1)
    q2(d2, 0, size - 1, s2)
    q3(d3, 0, size - 1, s3)
    print(f"s1 is {s1.count}")
    print(f"s2 is {s2.count}")
    print(f"s3 is {s3.count}")
