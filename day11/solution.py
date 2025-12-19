# Advent of Code 2025 - Day 11

lines = open('input.txt').read().strip().split('\n')

graph = {}
for line in lines:
    segments = line.split(" ")
    ins = segments[0][:-1]
    outs = segments[1:]
    for out in outs:
        if ins in graph:  
            graph[ins].append(out)
        else: 
            graph[ins] = []
            graph[ins].append(out)
# Part 1
def part1():
    def DFS(node):
        if node == "out":
            return 1
        
        return sum([DFS(neighbor) for neighbor in graph.get(node, [])])
    
    print(DFS("you"))

# Part 2
def part2():
    cache = {}

    def DFS(node, has_dac, has_fft):

        key = (node, has_dac, has_fft)

        if key in cache: 
            return cache[key]

        if node == "out":
            return 1 if has_dac and has_fft else 0

        total = 0
        for neighbor in graph.get(node, []):
            total += DFS(neighbor, has_dac or (neighbor == "dac"), has_fft or (neighbor == "fft"),)

        cache[key] = total
        return total

    print(DFS("svr", False, False))

if __name__ == '__main__':
    part1()
    part2()
