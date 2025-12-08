# Advent of Code 2025 - Day 7

grid = []

with open('input.txt') as file: 
    grid = [list(line) for line in file.read().strip().split('\n')]

beam_start = (1, grid[0].index('S'))

def in_bounds(location):
    height = len(grid)
    width = len(grid[0])
    return location[0] >= 0 and location[0] < height and location[1] >= 0 and location[1] < width

# Part 1
def part1():  
    def count_splits(location, split_locations):
        if grid[location[0]][location[1]] == "^":
            
            if location in split_locations:
                return 0
            
            split_locations.add(location)

            left = (location[0] + 1, location[1] - 1)
            right = (location[0] + 1, location[1] + 1)
            
            count = 1
            if in_bounds(left):
                count += count_splits(left, split_locations)
            if in_bounds(right):
                count += count_splits(right, split_locations)
            return count
            
        new_location = (location[0] + 1, location[1])
        if in_bounds(new_location):
            return count_splits(new_location, split_locations)
        return 0

    print(count_splits(beam_start, set()))

# Part 2
def part2():
    def count_timelines(location, timelines):
        if not in_bounds(location):
            return 1 

        if location in timelines:
            return timelines[location]
        
        if grid[location[0]][location[1]] == "^":
            left = (location[0] + 1, location[1] - 1)
            right = (location[0] + 1, location[1] + 1)
            result = count_timelines(left, timelines) + count_timelines(right, timelines)
            timelines[location] = result
            return result
        elif grid[location[0]][location[1]] == ".":
            new_location = (location[0] + 1, location[1])
            result = count_timelines(new_location, timelines)
            timelines[location] = result
            return result
        
        return 0 
            
    print(count_timelines(beam_start, {}))

if __name__ == '__main__':
    part1()
    part2()
