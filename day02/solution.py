# Advent of Code 2025 - Day 2
lines = []

with open('input.txt') as file: 
    lines = file.read().strip().split(',')

# Part 1
def part1():
    invalid_ids = []

    for line in lines:
        start, end =  [int(x) for x in line.split('-')]
        for id in range(start, end+1, 1):
            id_str = str(id)
            n = len(id_str)
            if n % 2 == 1: # odd numbers are always valid. (Grayson)
                continue

            mid =  n // 2
            left = id_str[:mid]
            right = id_str[mid:]

            if left == right:
                invalid_ids.append(id)

    result = sum(invalid_ids)
    print(result)

# Part 2
def part2():
    invalid_ids = []

    for line in lines:
        start, end =  [int(x) for x in line.split('-')]
        for id in range(start, end+1, 1):
            id_str = str(id)
            n = len(id_str)

            # sliding window
            for window in range(1, n//2+1):
                if n % window == 0:
                    pattern = id_str[:window]
                    repetitions = n // window

                    if pattern * repetitions == id_str:
                        # print(pattern * repetitions, id_str)
                        invalid_ids.append(id)
                        break
            
    result = sum(invalid_ids)
    print(result)

if __name__ == '__main__':
    part1()
    part2()