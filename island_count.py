import queue

grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]


def create_graph(grid):
    graph = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "L":
                if (f"{r}, {c}") not in graph:
                    graph[(f"{r}, {c}")] = []
                if r > 0 and grid[r - 1][c] == "L":
                    graph[(f"{r}, {c}")].append(f"{r - 1}, {c}")
                if r < len(grid) - 1 and grid[r + 1][c] == "L":
                    graph[(f"{r}, {c}")].append(f"{r + 1}, {c}")
                if c > 0 and grid[r][c - 1] == "L":  # Fixed this check
                    graph[(f"{r}, {c}")].append(f"{r}, {c - 1}")
                if c < len(grid[r]) - 1 and grid[r][c + 1] == "L":
                    graph[(f"{r}, {c}")].append(f"{r}, {c + 1}")
    return graph


def count_islands(graph):
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            count += 1
            visited.add(node)
            myq = queue.Queue()
            myq.put(node)
            while not myq.empty():
                current = myq.get()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        myq.put(neighbor)
    return count


def island_count(grid):
    graph = create_graph(grid)
    print(graph)
    return count_islands(graph)


print(island_count(grid))  # -> 3
