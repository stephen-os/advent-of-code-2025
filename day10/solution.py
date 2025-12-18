# Advent of Code 2025 - Day 10
# Solution Credit: https://github.com/pemoreau/advent-of-code/blob/main/go/2025/10/day10.go

lines = open('input.txt').read().strip().split('\n')

schematics = [] 
for line in lines:
    i, j = line.find('[') + 1, line.rfind(']')
    lights = [c == '#' for c in line[i:j]]

    i, j = line.find('('), line.rfind(')') + 1
    buttons = [[int(value) for value in button[1:-1].split(',')] for button in line[i:j].split(' ')]    

    i, j = line.find('{') + 1, line.rfind('}')
    joltage = [int(jolt) for jolt in line[i:j].split(',')]
    
    schematics.append((lights, buttons, joltage))

class ButtonCombination:
    def __init__(self, counter, nb_pressed_buttons):
        self.counter = counter
        self.nb_pressed_buttons = nb_pressed_buttons

def smaller_or_equal(a, b):
    """Check if counter a is smaller or equal to counter b element-wise"""
    return all(a[i] <= b[i] for i in range(len(a)))

def equals_modulo_2(a, b):
    """Check if counters a and b are equal modulo 2"""
    return all(a[i] % 2 == b[i] % 2 for i in range(len(a)))

def is_zero(counter):
    """Check if all elements in counter are zero"""
    return all(c == 0 for c in counter)

def all_combinations(buttons, m):
    """Generate all possible button combinations"""
    nb_buttons = len(buttons)
    if nb_buttons == 0:
        return [ButtonCombination([0] * m, 0)]
    
    res = []
    for n in range(1 << nb_buttons):  # 2^nb_buttons combinations
        counter = [0] * m
        nb_pressed_buttons = 0
        for j in range(nb_buttons):
            if (n & (1 << j)) != 0:
                nb_pressed_buttons += 1
                for idx in buttons[j]:
                    counter[idx] += 1
        res.append(ButtonCombination(counter, nb_pressed_buttons))
    return res

def solve1(goal, combinations):
    """Find minimum button presses matching goal modulo 2"""
    res = float('inf')
    for comb in combinations:
        if equals_modulo_2(comb.counter, goal):
            if comb.nb_pressed_buttons < res:
                res = comb.nb_pressed_buttons
    return res

def solve2(counter, combinations):
    """Recursively solve for exact counter match"""
    if is_zero(counter):
        return 0, True
    
    res = float('inf')
    for comb in combinations:
        if not smaller_or_equal(comb.counter, counter):
            continue
        if not equals_modulo_2(comb.counter, counter):
            continue
        
        next_counter = [(counter[i] - comb.counter[i]) // 2 for i in range(len(counter))]
        rec, ok = solve2(next_counter, combinations)
        if not ok:
            continue
        
        n = 2 * rec + comb.nb_pressed_buttons
        if n < res:
            res = n
    
    if res < float('inf'):
        return res, True
    return 0, False

# Part 1
def part1():
    total = 0
    for lights, buttons, joltage in schematics:
        goal = [1 if light else 0 for light in lights]
        combinations = all_combinations(buttons, len(joltage))
        n = solve1(goal, combinations)
        total += n
    print(f"Part 1: {total}")

# Part 2
def part2():
    total = 0
    for lights, buttons, joltage in schematics:
        combinations = all_combinations(buttons, len(joltage))
        n, _ = solve2(joltage, combinations)
        total += n
    print(f"Part 2: {total}")

if __name__ == '__main__':
    part1()
    part2()