graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
  }

def connected_components_count(graph):
  from collections import deque
  visited = set()
  count = 0
  for node in graph:
    if node not in visited:
      count += 1
      visited.add(node)
      queue = deque()
      for node in graph[node]:
          queue.append(node)
          while (len(queue) > 0):
              current = queue.pop()
              visited.add(current)
              for neighbor in graph[current]:
                  if neighbor not in visited and neighbor not in queue:
                      queue.appendleft(neighbor)
  return count
    
print(connected_components_count(graph))