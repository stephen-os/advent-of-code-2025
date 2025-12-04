# Advent of Code 2025 - Day 3

lines = []

with open('input.txt') as file: 
    lines = file.read().strip().split('\n')

# Part 1
def part1():
    results = []
    for line in lines:
        n = len(line)
        max_left = n * [0]
        max_right = n * [0]

        max_left[0] = int(line[0])
        for i in range(1, n):
            max_left[i] = max(int(line[i]), max_left[i - 1]) 

        max_right[n-1] = int(line[n-1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(int(line[i]), max_right[i + 1])

        largest = -1
        for i in range(1, n):
            left_digit = max_left[i-1]
            right_digit = max_right[i]
            largest = max(largest, (10 * left_digit) + right_digit)

        results.append(largest)
    
    print(sum(results))

# Part 2
def part2():
    results = []
    for line in lines:
        n = len(line)
        k = 12
        
        dp = [["" for _ in range(k + 1)] for _ in range(n + 1)]
        
        for pos in range(n - 1, -1, -1):
            for picked in range(k + 1):
                if picked == 0:
                    dp[pos][picked] = ""
                    continue
                
                best = ""
                for i in range(pos, n - picked + 1):
                    if picked == 1:
                        candidate = line[i]
                    else:
                        candidate = line[i] + dp[i + 1][picked - 1]
                    
                    if candidate and (not best or candidate > best):
                        best = candidate
                
                dp[pos][picked] = best
                
        results.append(int(dp[0][k]))

    print(sum(results))    

if __name__ == '__main__':
    # part1()
    part2()
