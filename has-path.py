from collections import deque

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

input = "i", "j"

# Breadthfirst search as a queue
def has_path_breadth(graph, src, dst):
    if src == dst:
        return True
    queue = deque(src)
    while (len(queue) > 0):
        current = queue.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.appendleft(neighbor)
            has_path_breadth(graph, neighbor, dst)
    return False

print("Breadth first search")
print(has_path_breadth(graph, input[0], input[1]))


# Depthfirst search as a stack
def has_path_depth(graph, src, dst):
    if src == dst:
        return True
    queue = deque(src)
    while (len(queue) > 0):
        current = queue.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
            has_path_depth(graph, neighbor, dst)
    return False
print("Depth first search")
print(has_path_depth(graph, input[0], input[1]))