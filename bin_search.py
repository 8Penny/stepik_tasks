import sys
import math


def search_eq_ind(n, a):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = math.floor((l + r) / 2)
        if a[mid] == n:
            return mid
        if a[mid] > n:
            r = mid - 1
        else:
            l = mid + 1
    return -2


def get_eq_indexes(a, b):
    result = []
    for num in b:
        raw_index = search_eq_ind(num, a)
        result.append(raw_index + 1)
    return result


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n, *a = next(reader)
    k, *b = next(reader)
    assert len(a) == n
    assert len(b) == k
    indexes = get_eq_indexes(a, b)
    str_indexes = list(map(str, indexes))
    print(" ".join(str_indexes))


if __name__ == "__main__":
    main()
