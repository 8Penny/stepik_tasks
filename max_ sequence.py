import sys


def get_max_seq_len(nums):
    d = [1] * len(nums)
    for i in range(0, len(nums)):
        for j in range(0, i):
            rem = nums[i] % nums[j]
            if rem == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    max = 1
    for count in d:
        if count > max:
            max = count
    return max


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n = next(reader)
    nums = list(next(reader))
    answer, *_ = next(reader)

    result = get_max_seq_len(nums)
    assert result == answer


if __name__ == "__main__":
    main()
