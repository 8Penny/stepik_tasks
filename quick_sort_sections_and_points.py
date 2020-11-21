#  Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
import sys
import random
import operator
import math


def bin_search_ind(a, n, relate=operator.lt, index=0):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = math.floor((l + r) / 2)
        if relate(n, a[mid][index]):
            r = mid - 1
        else:
            l = mid + 1

    return l


def partition(sections, l, r, sort_ind=0, relate=operator.lt):
    if relate != operator.eq:
        support_ind = random.randint(l, r)
        sections[l], sections[support_ind] = sections[support_ind], sections[l]

    support_element = sections[l][sort_ind]
    current_ind = l + 1
    threshold = l

    while current_ind < r + 1:
        if relate(sections[current_ind][sort_ind], support_element):
            threshold += 1
            sections[threshold], sections[current_ind] = sections[current_ind], sections[threshold]
        current_ind += 1

    sections[threshold], sections[l] = sections[l], sections[threshold]
    return threshold


def sections_quick_sort(sections, l, r, sort_ind=0):
    if l >= r:
        return
    new_r = partition(sections, l, r, sort_ind)
    new_l = partition(sections, new_r, r, sort_ind, operator.eq)
    sections_quick_sort(sections, l, new_r - 1, sort_ind)
    sections_quick_sort(sections, new_l + 1, r, sort_ind)


def get_occurrences_count(sections, points):
    tail_sorted_sections = sections.copy()
    last_index = len(sections) - 1
    sections_quick_sort(sections, 0, last_index)
    sections_quick_sort(tail_sorted_sections, 0, last_index, 1)

    result = []
    for point in points:
        ind_1 = bin_search_ind(tail_sorted_sections, point, operator.le, 1)
        ind_2 = bin_search_ind(sections, point, operator.lt)
        result.append(ind_2 - ind_1)
    return " ".join(map(str, result))


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n, m = next(reader)
    sections = []
    for sec in range(0, n):
        sections.append(list(next(reader)))
    points = list(next(reader))

    occ_count = get_occurrences_count(sections, points)
    print(occ_count)


if __name__ == "__main__":
    main()
