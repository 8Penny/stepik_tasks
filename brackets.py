import sys


def is_match(open_b, close_b):
    if open_b == "[":
        return close_b == "]"
    if open_b == "(":
        return close_b == ")"
    if open_b == "{":
        return close_b == "}"


def check_sequence(brackets):
    open_brackets_stack = []
    open_b = ("[", "(", "{")
    close_b = ("]", ")", "}")
    for ind in range(0, len(brackets)):
        if brackets[ind] in open_b:
            open_brackets_stack.append([brackets[ind], ind + 1])
        elif brackets[ind] in close_b:
            if len(open_brackets_stack) == 0:
                return ind + 1
            if is_match(open_brackets_stack[-1][0], brackets[ind]):
                open_brackets_stack.pop()
                continue
            return ind + 1
    if len(open_brackets_stack) != 0:
        return open_brackets_stack.pop()[1]
    return "Success"


def main():
    f = open(sys.argv[1], "r")
    brackets_sequence = f.readline()
    result = check_sequence(brackets_sequence)
    print(result)


if __name__ == "__main__":
    main()