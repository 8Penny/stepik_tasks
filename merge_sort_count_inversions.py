# Необходимо посчитать число инверсий
import sys


def calculate_inv_count(a):
    result = 0
    heap = []
    for el in a:
        heap.append([el])

    heap_len = len(heap)
    heap_start_index = 0

    while heap_len > 1:
        if heap_len >= 2 and len(heap[heap_start_index]) < len(heap[heap_start_index+1]):
            tail = heap[heap_start_index]
            heap.append(tail)
            fst = heap[heap_start_index + 1]
            snd = heap[heap_start_index + 2]
            heap_start_index += 3

        else:
            fst = heap[heap_start_index]
            snd = heap[heap_start_index + 1]
            heap_start_index += 2

        merged = []
        help_inv_parameter = 0

        fst_start = 0
        snd_start = 0
        fst_len = len(fst)
        snd_len = len(snd)

        while True:
            if fst[fst_start] <= snd[snd_start]:
                merged.append(fst[fst_start])
                fst_start += 1
            else:
                merged.append(snd[snd_start])
                snd_start += 1
                help_inv_parameter += fst_len - fst_start

            if fst_len - fst_start == 0:
                merged += snd[snd_start:]
                break
            if snd_len - snd_start == 0:
                merged += fst[fst_start:]
                break

        heap.append(merged)
        heap_len -= 1
        result += help_inv_parameter

    return result


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())

    test_count, *_ = next(reader)
    for i in range(test_count):
        n, *_ = next(reader)
        a = list(next(reader))
        answer, *_ = next(reader)
        assert len(a) == n

        inv_count = calculate_inv_count(a)
        print("answer: {}  inv count: {}".format(answer, inv_count))
        assert answer == inv_count


if __name__ == "__main__":
    main()
