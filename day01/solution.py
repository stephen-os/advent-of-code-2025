# Advent of Code 2025 - Day 1

lines = open('input.txt').read().strip().split('\n')

# Part 1
def part1():
    dial_position = 50
    password = 0 

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "R":
            dial_position = (dial_position + distance) % 100
        else:
            dial_position = (dial_position - distance) % 100

        if dial_position == 0:
            password += 1

    print(password)

# Part 2
def part2():

    dial_position = 50
    password = 0 

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        while distance > 99: # no matter what, all rotation will result in crossing 0
            password += 1 
            distance -= 100

        # print(dial_position, direction, distance, password)
        if direction == "R":
            prev_dial_position = dial_position

            dial_position = (dial_position + distance) % 100

            if dial_position < prev_dial_position and prev_dial_position != 0: # we have rotated past 99 so we must be at or have passed 0
                password += 1
                continue
        else:
            prev_dial_position = dial_position
            dial_position = (dial_position - distance) % 100

            if dial_position > prev_dial_position and prev_dial_position != 0:
                password += 1
                continue
            
        if dial_position == 0:
           password += 1

    print(password)

if __name__ == '__main__':
    part1()
    part2()

lines.close()