# Advent of Code 2025 - Day 9

from collections import deque

lines = []
with open('input.txt') as file: 
    lines = file.read().strip().split('\n')

tile_positions = []
for line in lines:
    x, y = [int(c) for c in line.split(',')]
    tile_positions.append((x, y))

def tile_area(position1, position2):
    w = abs(position1[0] - position2[0] + 1)
    h = abs(position1[1] - position2[1] + 1)
    return w * h

# Part 1
def part1():
    n = len(tile_positions)
    max_area = 0 
    for i in range(n):
        for j in range(i, n):
            a = tile_area(tile_positions[i], tile_positions[j])
            max_area = max(max_area, a)
    print(max_area)

# Part 2
def part2():
    pass
    
if __name__ == '__main__':
    part1()
    part2()
