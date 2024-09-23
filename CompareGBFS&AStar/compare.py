import time
import csv
from heapq import heappush, heappop

def read_grid(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node, grid):
    x, y = node
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.':
            yield (nx, ny)

def gbfs(start, goal, grid):
    open_set = []
    heappush(open_set, (heuristic(start, goal), start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_set:
        _, current = heappop(open_set)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1], cost_so_far[goal]
        
        for next in neighbors(current, grid):
            if next not in cost_so_far:
                came_from[next] = current
                cost_so_far[next] = cost_so_far[current] + 1
                heappush(open_set, (heuristic(next, goal), next))
                
    return None, float('inf')

def astar(start, goal, grid):
    open_set = []
    heappush(open_set, (0 + heuristic(start, goal), start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_set:
        _, current = heappop(open_set)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1], cost_so_far[goal]
        
        for next in neighbors(current, grid):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                came_from[next] = current
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                heappush(open_set, (priority, next))
                
    return None, float('inf')

# Read the grid
grid = read_grid('../Test 4.txt')

# Define the pairs of start and goal points
pairs = [
    ((178, 180), (176, 180)),
    ((380, 313), (384, 300)),
    ((675, 635), (739, 627)),
    ((492, 168), (578, 88)),
    ((166, 284), (194, 137)),
    ((622, 785), (400, 190)),
    ((79, 847), (936, 594)),
    ((191, 139), (799, 1007)),
    ((837, 776), (1, 102)),
    ((3, 19), (1002, 1005))
]

results = []

for start, goal in pairs:
    # Measure GBFS
    start_time = time.time()
    path_gbfs, cost_gbfs = gbfs(start, goal, grid)
    time_gbfs = time.time() - start_time
    
    # Measure A*
    start_time = time.time()
    path_astar, cost_astar = astar(start, goal, grid)
    time_astar = time.time() - start_time
    
    results.append((start, goal, cost_gbfs, time_gbfs, cost_astar, time_astar))

# Save results to a CSV file
with open('./results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Start', 'Goal', 'GBFS Cost', 'GBFS Time (s)', 'A* Cost', 'A* Time (s)'])
    for start, goal, cost_gbfs, time_gbfs, cost_astar, time_astar in results:
        writer.writerow([start, goal, cost_gbfs, time_gbfs, cost_astar, time_astar])

# Print the results to verify
for i, (start, goal, cost_gbfs, time_gbfs, cost_astar, time_astar) in enumerate(results):
    print(f"Pair {i + 1}:")
    print(f"  Start: {start}, Goal: {goal}")
    print(f"  GBFS - Cost: {cost_gbfs}, Time: {time_gbfs:.4f}s")
    print(f"  A* - Cost: {cost_astar}, Time: {time_astar:.4f}s")
    print()
