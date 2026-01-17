# REPRESENTASI GRAF
graph = (
  'A':['B','C']
  'B':['A','C','D']
  'C':['A','B','D']
  'D':['B','C']
)

# SPANNING TREE MENGGUNAKAN DFS
def dfs_spanning_tree(graph, start):
  visited=set()
  spanning_tree=[]

  def dfs(u):
    visited.add(u)
    for v in graph(u)
      if v not in visited:
        spanning_tree.append((u,v))
        dfs (v)

dfs (start)
return spanning_tree

## PEMANGGILAN
tree = dfs_spanning_tree(graph, 'A')
print("Spanning Tree (DFS):")
print(tree)

# SPANNING TREE MENGGUNAKAN BFS
from collections import deque

def bfs_spanning_tree(graph, start)
  visited = set ([start])
  queue = deque([start])
  spanning_tree = []

  while queue:
    u = queue.popleft()
    for  v in graph[u]:
      if v not in visited:
        visited.add(v)
        queue..append(v)
        spanning_tree.append((u,v))
  return spanning_tree

## PEMANGGILAN
tree = bfs_spanning_tree(graph, 'A')
print("Spanning Tree (BFS):")
print(tree)
