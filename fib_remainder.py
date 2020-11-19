#  Даны целые числа 1 ≤ n ≤ 10^{18} и 2 ≤ m ≤ 10^5 , необходимо найти остаток от деления n-го числа Фибоначчи на m.
import sys


def find_remainder(n, m):
    if n < 2:
        n - 1

    rems = [0, 1]

    was_first_match = False
    i = 2
    while i <= n:
        c = (rems[-1] + rems[-2]) % m
        rems.append(c)
        is_last_eq_first = c == 0
        if was_first_match:
            if c == 1:
                period = i - 1
                return rems[n % period]
            was_first_match = False
        elif is_last_eq_first:
            was_first_match = True

        i += 1

    return rems[-1]


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n, m = next(reader)
    assert m >= 2

    rem = find_remainder(n, m)
    print(rem)


if __name__ == "__main__":
    main()
