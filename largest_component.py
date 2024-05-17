from collections import deque

graph_6 = {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
graph_2 = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}


def find_node_size(graph, node, visited):
    count = 0
    queue = deque()
    queue.append(node)
    while len(queue) > 0:
        count += 1
        current = queue.pop()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.appendleft(neighbor)
    return count


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        if node not in visited:
            count = find_node_size(graph, node, visited)
            if count > largest:
                largest = count
    return largest


print("Graph 6")  # this is a single component with 6 nodes
print(largest_component(graph_6))
print("Graph 4")  # this is 2 compoenents, 1 with 4 and 1 with 3
print(largest_component(graph_2))
