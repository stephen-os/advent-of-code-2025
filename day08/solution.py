import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

# Advent of Code 2025 - Day 8

positions = []
with open('input.txt') as file: 
    lines = file.read().strip().split('\n')
    positions = [tuple(int(coord) for coord in line.split(',')) for line in lines]

"""
# For fun

positions = np.array(positions)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], 
                     c=positions[:, 2], cmap='viridis', s=20, alpha=0.6)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title(f'3D Coordinate Visualization ({len(positions)} points)', fontsize=14)

ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])
ax.set_zlim([0, 1000])

cbar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
cbar.set_label('Z value', fontsize=10)

ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
"""

def euclidean_distance(vertex1, vertex2):
    return math.sqrt(math.pow(vertex1[0] - vertex2[0], 2) + math.pow(vertex1[1] - vertex2[1], 2) + math.pow(vertex1[2] - vertex2[2], 2))

# Part 1
def part1():
    distances = []
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(positions[i], positions[j])
            distances.append((positions[i], positions[j], distance))
   
    distances = sorted(distances, key=lambda item: item[2])

    circuits = {position: {position} for position in positions}
    attempts = 0

    for position1, position2, distance in distances:

        if attempts >= 1000:
            break
    
        attempts += 1

        if circuits[position1] is circuits[position2]:
            continue

        merged = circuits[position1] | circuits[position2]

        for position in merged:
            circuits[position] = merged
        
    unique_circuits = set()
    for circuit in circuits.values():
        unique_circuits.add(frozenset(circuit))

    sizes = sorted([len(circuit) for circuit in unique_circuits], reverse=True)    
    result = math.prod(sizes[:3])
    print(result)

# Part 2
def part2():
    distances = []
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(positions[i], positions[j])
            distances.append((positions[i], positions[j], distance))
    
    distances = sorted(distances, key=lambda item: item[2])
    
    circuits = {position: {position} for position in positions}
    edges_added = 0
    
    for position1, position2, distance in distances:
        if circuits[position1] is circuits[position2]:
            continue
        
        merged = circuits[position1] | circuits[position2]
        
        for position in merged:
            circuits[position] = merged
        
        edges_added += 1
        
        if edges_added == n - 1:
            print(position1[0] * position2[0])
            break
    
if __name__ == '__main__':
    part1()
    part2()
