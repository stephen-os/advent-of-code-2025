# Advent of Code 2025 - Day 4

lines = []

with open('input.txt') as file: 
    lines = file.read().strip().split('\n')

grid = []

for line in lines:
    grid.append(list(line))

# Part 1
def part1():
    n = len(grid)
    m = len(grid[0])

    directions = [
        ( 1,  0),
        (-1,  0),
        ( 0,  1),
        ( 0, -1),
        ( 1,  1),
        (-1,  1),
        ( 1, -1),
        (-1, -1)
        ]
    
    can_access = 0 
    
    def inbounds(a, b):
        return a >= 0 and b >= 0 and a < n and b < m

    for i in range(n):
        for j in range(m):
            if grid[i][j] != '@':
                continue

            adjacent_roll = 0

            for d in directions: 
                a, b = i + d[0], j + d[1]
                if inbounds(a, b) and grid[a][b] == "@":
                    adjacent_roll += 1
                    
            if adjacent_roll < 4: 
                can_access += 1
                
    print(can_access)
    pass

# Part 2
def part2():

    last_result = -1
    result = []
    while last_result != 0: 
        n = len(grid)
        m = len(grid[0])

        directions = [
            ( 1,  0),
            (-1,  0),
            ( 0,  1),
            ( 0, -1),
            ( 1,  1),
            (-1,  1),
            ( 1, -1),
            (-1, -1)
            ]
        
        can_access = 0 
        can_remove = []
        
        def inbounds(a, b):
            return a >= 0 and b >= 0 and a < n and b < m

        for i in range(n):
            for j in range(m):
                if grid[i][j] != '@':
                    continue

                adjacent_roll = 0

                for d in directions: 
                    a, b = i + d[0], j + d[1]
                    if inbounds(a, b) and grid[a][b] == "@":
                        adjacent_roll += 1
                        
                if adjacent_roll < 4: 
                    can_access += 1
                    can_remove.append((i, j))
        
        last_result = can_access
        result.append(last_result)

        for i, j in can_remove: 
            grid[i][j] = '.'

        # for row in grid:
            # print("".join(row))
    
    print(sum(result))
                
    pass

if __name__ == '__main__':
    part1()
    part2()
