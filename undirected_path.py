from collections import deque

input = "m", "j"

# This is a list of edges, we need to find the nodes
# Once we find the nodes we need to map their adjacency

# Here we create placehoders and add any data we have already
graph = {}
nodes = []
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
# Since we don't know if this is acyclic then we need to prevent loops


# Lets iterate through the edges list and pull out the individual nodes
# While we do this we can build out the adjacency graph
for edge in edges:
    node1, node2 = edge
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

# Now that we have the graph we can use the 'has_path" algo to find a path
# We have added the 'visited' portion to keep track if we've been there before
def has_path_breadth(graph, src, dst):
    if src == dst:
        return True
    queue = deque(src)
    visited = set()
    while (len(queue) > 0):
        current = queue.popleft()
        if current == dst:
            return True
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.appendleft(neighbor)
    return False

print("Breadth first search")
print(has_path_breadth(graph, input[0], input[1]))