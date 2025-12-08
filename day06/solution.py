import math

# Advent of Code 2025 - Day 6

def parse_input_file(filename="input.txt"):
    with open(filename) as f:
        lines = f.read().rstrip("\n").split("\n")

    number_lines = lines[:-1]
    operator_line = lines[-1]

    max_len = max(len(line) for line in lines)
    grid = [list(line.ljust(max_len)) for line in number_lines]
    ops  = list(operator_line.ljust(max_len))

    separator_cols = []
    for c in range(max_len):
        if all(row[c] == ' ' for row in grid):
            separator_cols.append(c)

    separators = []
    if separator_cols:
        start = separator_cols[0]
        prev  = start
        for c in separator_cols[1:]:
            if c == prev + 1:
                prev = c
            else:
                separators.append((start, prev))
                start = c
                prev = c
        separators.append((start, prev))

    segments = []
    prev_end = 0

    if separators:
        for start, end in separators:
            if start > prev_end:
                segments.append((prev_end, start - 1))
            prev_end = end + 1
        if prev_end < max_len:
            segments.append((prev_end, max_len - 1))
    else:
        segments = [(0, max_len - 1)]

    problems = []
    for a, b in segments:
        nums = [''.join(row[a:b+1]) for row in grid]
        op   = ''.join(ops[a:b+1]).strip()  # strip spaces → operator symbol

        problems.append((nums, op))

    return problems


def transform_problems(problems):
    t_problems = []

    for nums, op in problems:
        rows = len(nums)
        cols = len(nums[0])
        new_nums = []

        for c in range(cols):
            col_chars = [nums[r][c] for r in reversed(range(rows))]
            s = ''.join(col_chars)[::-1]
            new_nums.append(s)

        t_problems.append((new_nums, op))

    return t_problems

problems = parse_input_file()
t_problems = transform_problems(problems)

# Part 1
def part1():
    grand_total = 0
    for problem in problems:

        operands = [int(operand.strip()) for operand in problem[0]]

        match problem[1]:
            case "+":
                grand_total += sum(operands)
            case "*":
                grand_total += math.prod(operands)

    print(grand_total)

# Part 2
def part2():
    grand_total = 0
    for problem in t_problems:

        operands = [int(operand.strip()) for operand in problem[0]]

        match problem[1]:
            case "+":
                grand_total += sum(operands)
            case "*":
                grand_total += math.prod(operands)

    print(grand_total)
    pass

if __name__ == '__main__':
    part1()
    part2()