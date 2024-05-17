import queue

grid = [
    ["L", "L", "L"],
    ["L", "L", "L"],
    ["L", "L", "L"],
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


def find_node_size(graph, node, visited):
    count = 0
    myq = queue.Queue()
    myq.put(node)
    visited.add(node)
    while not myq.empty():
        count += 1
        current = myq.get()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                myq.put(neighbor)
    return count


def largest_component(graph):
    visited = set()
    smallest = 50000
    for node in graph:
        if node not in visited:
            count = find_node_size(graph, node, visited)
            if count < smallest:
                smallest = count
    return smallest


def island_count(grid):
    graph = create_graph(grid)
    print(graph)
    return largest_component(graph)


print(island_count(grid))  # -> 3
