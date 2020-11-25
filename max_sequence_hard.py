import sys
import math


# def bin_search(number, array, l, r):
#     while l <= r:
#         mid = math.floor((l + r) / 2)
#         if array[mid][0] >= number:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return l
def bin_search(number, array, l, r):
    while l <= r:
        mid = math.floor((l + r) / 2)
        if array[mid][0] <= number:
            r = mid - 1
        else:
            l = mid + 1
    return l


def find_max_seq(nums):
    help_len = len(nums) + 1
    help = []
    for i in range(0, help_len):
        help.append([-math.inf, -1])

    help[0][0] = math.inf

    seq = []
    d = [-1] * (help_len - 1)
    result_count = 0

    for ind in range(0, len(nums)):
        element = [nums[ind], ind]
        replace_ind = bin_search(element[0], help, 0, help_len)
        if help[replace_ind][0] == -math.inf:
            seq.append(element)
            result_count += 1
        old_element = help[replace_ind]

        help[replace_ind] = element
        if old_element[0] == element[0]:
            d[ind] = old_element[1]
        else:
            d[ind] = help[replace_ind - 1][1]
    result = [0] * help_len
    ind = help[result_count][1]

    print(help)
    print(d)

    search = False
    for i in range(ind + 1, len(d)):
        if ind == d[i] + 1:
            t = ind + 1
            search = True
        if search and t == d[i]:
            t += 1

    if search:
        ind = t

    i = -1
    c = 0

    while ind != -1:
        prev = ind
        other_len = 0

        for j in range(prev + 1, len(d) - 1):

            if prev == d[j + 1]:
                prev = j + 1
                other_len += 1

        if c < other_len:
            ind = prev
            i = -1
            c = 0
        result[i] = ind + 1
        ind = d[ind]
        i -= 1
        c += 1
    result = result[-c:]
    return len(result), result


def get_max_seq(nums):

    d = [1] * len(nums)
    for i in range(0, len(nums)):
        for j in range(0, i):
            is_ok = nums[j] >= nums[i]
            if is_ok and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    max_ind = 0
    for ind in range(0, len(d)):
        if d[ind] > d[max_ind]:
            max_ind = ind

    result = [0] * d[max_ind]
    next_threshold = d[max_ind]
    empty_tail_ind = d[max_ind] - 1
    for i in range(max_ind, -1, -1):
        if d[i] == next_threshold:
            result[empty_tail_ind] = i + 1
            empty_tail_ind -= 1
            next_threshold -= 1
    return d[max_ind], result


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n = next(reader)
    nums = list(next(reader))
    #answer, *_ = next(reader)
    #answer_seq = list(next(reader))

    result, result_seq = find_max_seq(nums)
    print(result)
    print(result_seq)
    #print(answer_seq)
    #print("{} {}".format(nums[answer_seq[-1]], nums[result_seq[-1]]))
    #assert result == answer
    #assert result_seq == answer_seq

    #print(bin_search(21, [-math.inf, 0, 1, 4, 5, 8, 21], 0, 6))


if __name__ == "__main__":
    main()
