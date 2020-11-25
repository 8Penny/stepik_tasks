import sys


def calculate_sequences_difference(a, b):
    a_len = len(a)
    b_len = len(b)

    l1 = range(0, a_len + 1)

    for i in range (1, b_len + 1):
        l2 = [i]
        for j in range(1, a_len + 1):
            a_letter = a[j - 1]
            b_letter = b[i - 1]
            diff = 0 if a_letter == b_letter else 1
            res = min(l2[j - 1] + 1, l1[j] + 1, l1[j - 1] + diff)
            l2.append(res)
        l1, l2 = l2, l1
    return l1[-1]


def main():
    f = open(sys.argv[1], "r")
    reader = (x.replace("\n", "") for x in f.readlines())
    a = next(reader)
    b = next(reader)
    answer = int(next(reader))
    result = calculate_sequences_difference(a, b)
    print(result)
    assert result == answer


if __name__ == "__main__":
    main()