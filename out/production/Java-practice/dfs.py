def dfs(graph,start):
    stack=[start]
    visited=set()
    while stack:
        node= stack.pop()
        if node not in  visited:
           visited.add(node)
           print(node,' ')

           for neighbour in reversed(graph[node] ):
                if neighbour not in visited:
                        stack.append(neighbour)

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}    

dfs(graph,'A')