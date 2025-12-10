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
    w = abs(position1[0] - position2[0]) + 1
    h = abs(position1[1] - position2[1]) + 1
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
    edges = []
    for i in range(len(tile_positions)):
        x1, y1 = tile_positions[i]
        x2, y2 = tile_positions[(i + 1) % len(tile_positions)]
        edges.append((x1, y1, x2, y2, i, (i+1) % len(tile_positions)))
    
    def rectangles_intersect(minX, minY, maxX, maxY, idx1, idx2):
        for x1, y1, x2, y2, edge_idx1, edge_idx2 in edges:
            if edge_idx1 in [idx1, idx2] or edge_idx2 in [idx1, idx2]:
                continue
                
            edge_minX = min(x1, x2)
            edge_maxX = max(x1, x2)
            edge_minY = min(y1, y2)
            edge_maxY = max(y1, y2)
            
            if minX < edge_maxX and maxX > edge_minX and minY < edge_maxY and maxY > edge_minY:
                return True
        return False
    
    max_area = 0
    n = len(tile_positions)
    
    for i in range(n):
        for j in range(i, n):
            p1 = tile_positions[i]
            p2 = tile_positions[j]
            
            minX = min(p1[0], p2[0])
            maxX = max(p1[0], p2[0])
            minY = min(p1[1], p2[1])
            maxY = max(p1[1], p2[1])
            
            if not rectangles_intersect(minX, minY, maxX, maxY, i, j):
                area = tile_area(p1, p2)
                if area > max_area:
                    max_area = area
    
    print(max_area)
    
if __name__ == '__main__':
    part1()
    part2()