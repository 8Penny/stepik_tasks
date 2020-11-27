import sys


def rec_calculate_max_sum(weights, l, r):
    if l == r:
        return weights[l]
    if l == r - 1:
        if weights[l + 1] < 0:
            return weights[l]
        return weights[l] + weights[l+1]
    next_sum = rec_calculate_max_sum(weights, l + 1, r)
    jump_sum = rec_calculate_max_sum(weights, l + 2, r)

    return max(next_sum, jump_sum) + weights[l]


def light_calculate_max_sum(weights):
    if len(weights) == 1:
        return weights[-1]
    n_step = weights[-1]
    prev_1 = weights[-2]
    prev_2 = 0
    for i in range(len(weights) - 3, -1, -1):
        temp = weights[i] + max(prev_1, prev_2)
        prev_2 = prev_1
        prev_1 = temp

    return max(prev_1, prev_2) + n_step


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n, *_ = next(reader)
    w = list(next(reader))
    answer, *_ = next(reader)
    #result = rec_calculate_max_sum(w, 0, len(w) - 1)
    result = light_calculate_max_sum(w)
    print(result)
    assert result == answer


if __name__ == "__main__":
    main()