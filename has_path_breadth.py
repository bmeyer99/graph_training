graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
import queue


def has_path(graph, src, dst):
    if src == dst:
        return True
    myq = queue.Queue()
    myq.put(src)
    while not myq.empty():
        current = myq.get()
        if current == dst:
            return True
        for neighbor in graph[current]:
            myq.put(neighbor)
            has_path(graph, neighbor, dst)
    return False


print(has_path(graph, "f", "k"))
