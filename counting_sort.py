import sys


def counting_sort(a):
    b = [0] * 10
    result = a.copy()
    for num in a:
        b[num - 1] += 1

    for i in range(1, 10):
        b[i] += b[i - 1]

    for j in range(len(a) - 1, -1, -1):
        result[b[a[j] - 1] - 1] = a[j]
        b[a[j] - 1] = b[a[j] - 1] - 1

    return result


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    nums = list(next(reader))
    answer = list(next(reader))

    result = counting_sort(nums)
    assert result == answer


if __name__ == "__main__":
    main()
