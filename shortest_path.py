import queue

# This is a list of edges, we need to find the nodes
# Once we find the nodes we need to map their adjacency

# Here we create placeholders and add any data we have already
edges_2_w_z = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
edges_1_y_x = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
edges_3_a_e = [
    ["a", "c"],
    ["a", "b"],
    ["c", "b"],
    ["c", "d"],
    ["b", "d"],
    ["e", "d"],
    ["g", "f"],
]
# Since we don't know if this is acyclic then we need to prevent loops


# Lets iterate through the edges list and pull out the individual nodes
# While we do this we can build out the adjacency graph and return it
def build_graph(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph


def get_path(graph, src, dst, visited=None, current=None):
    if visited is None:
        visited = set()

    if current is None:
        current = (src, 0)  # Initialize with source node and distance 0

    visited.add(src)

    if src == dst:
        return current[1]

    myq = queue.Queue()
    myq.put(current)

    while not myq.empty():
        current = myq.get()
        if current[0] == dst:
            return current[1]

        for neighbor in graph.get(current[0], []):
            if neighbor not in visited:
                visited.add(neighbor)
                myq.put((neighbor, current[1] + 1))

    return None


def shortest_path(edges, src, dst):
    graph = build_graph(edges)
    visited = set()
    return get_path(graph, src, dst, visited, current=(src, 0))


print("    ")
print("result should be 1 below")
print(shortest_path(edges_1_y_x, "y", "x"))
print("    ")
print("result should be 2 below")
print(shortest_path(edges_2_w_z, "w", "z"))
print("    ")
print("Result should be 3 below")
print(shortest_path(edges_3_a_e, "a", "e"))
