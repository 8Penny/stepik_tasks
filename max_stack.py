import sys

stack = []
stack_max = []


def push(el):
    stack.append(el)
    if not stack_max:
        stack_max.append(el)
        return
    if stack_max[-1] < el:
        stack_max.append(el)
    else:
        stack_max.append(stack_max[-1])


def pop():
    stack.pop()
    stack_max.pop()


def max():
    return stack_max[-1]


def main():
    f = open(sys.argv[1], "r")
    reader = (tuple(line.split()) for line in f.readlines())
    n, *_ = next(reader)
    n = int(n)

    for i in range(0, n):
        op = list(next(reader))
        if op[0] == "max":
            print(max())
        elif op[0] == "push":
            push(int(op[1]))
        else:
            pop()


if __name__ == "__main__":
    main()
