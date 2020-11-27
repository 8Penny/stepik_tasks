import sys


def get_max_deep(tree):
    help = []
    for j in range(0, len(tree)):
        help.append([])
    for i in range(0, len(tree)):
        if tree[i] == -1:
            root = i
            continue
        help[tree[i]].append(i)

    children = help[root]
    depth = 1
    while children:
        children2 = []
        depth += 1
        while children:
            children2 += help[children.pop()]
        children = children2

    return depth


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    n, *_ = next(reader)
    parent_data = list(next(reader))
    result = get_max_deep(parent_data)
    print(result)


if __name__ == "__main__":
    main()
