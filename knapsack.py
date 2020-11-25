import sys


def calculate_max_knapsack_weight(capacity, weights):
    d = []
    for i in range(0, len(weights) + 1):
        d.append([0] * (capacity + 1))

    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            d[i][j] = d[i - 1][j]
            if j >= weights[i - 1]:
                d[i][j] = max(d[i-1][j - weights[i - 1]] + weights[i - 1], d[i - 1][j])

    return d[-1][-1]


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    capacity, _ = next(reader)
    w = list(next(reader))
    answer, *_ = next(reader)
    result = calculate_max_knapsack_weight(capacity, w)
    print(result)
    assert result == answer


if __name__ == "__main__":
    main()