def DFS(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(neighbor, visited, graph)

def LienThong(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    
    start_node = next(iter(graph))
    
    DFS(start_node, visited, graph)
    
    return all(visited)

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("Đồ thị liên thông:", LienThong(graph))