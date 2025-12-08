# Advent of Code 2025 - Day 5

lines = []

with open('input.txt') as file: 
    lines = file.read().strip().split('\n')

split_index = lines.index('')
fresh_id_ranges = lines[:split_index]
print(fresh_id_ranges)
ids = lines[split_index+1:]


def is_fresh(id): 
    for r in fresh_id_ranges: 
        l, r = [int(x) for x in r.split('-')]
        if id >= l and id <= r:
            return True
    return False

# Part 1
def part1():
    fresh = 0
    for id in ids:
        if is_fresh(int(id)):
            fresh += 1
    
    print(fresh)

# Part 2
def part2():
    ranges = [tuple(map(int, r.split('-'))) for r in fresh_id_ranges]
    
    ranges.sort()

    merged = [ranges[0]]

    for start, end in ranges[1:]:
        ms, me = merged[-1]
        if start <= me:
            merged[-1] = (ms, max(me, end))
        else:
            merged.append((start, end))

    ids = 0
    for r in merged: 
        l, r = r
        ids += r - l + 1

    print(ids)
    
if __name__ == '__main__':
    part1()
    part2()
