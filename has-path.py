import queue

graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

input = "i", "j"


# Breadthfirst search as a myq
def has_path_breadth(graph, src, dst):
    if src == dst:
        return True
    myq = queue.Queue()
    while not myq.empty():
        current = myq.get()
        if current == dst:
            return True
        for neighbor in graph[current]:
            myq.put(neighbor)
            has_path_breadth(graph, neighbor, dst)
    return False


print("Breadth first search")
print(has_path_breadth(graph, input[0], input[1]))


# Depthfirst search as a stack
def has_path_depth(graph, src, dst):
    if src == dst:
        return True
    myq = queue.Queue
    while len(myq) > 0:
        current = myq.get()
        if current == dst:
            return True
        for neighbor in graph[current]:
            myq.append(neighbor)
            has_path_depth(graph, neighbor, dst)
    return False


print("Depth first search")
print(has_path_depth(graph, input[0], input[1]))
