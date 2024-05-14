def DFS(node, visited, parent, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            if DFS(neighbor, visited, parent, graph):
                return True
        elif parent[node] != neighbor:
            return True
    return False

def ChuTrinh(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    parent = [-1] * num_nodes
    
    for node in range(num_nodes):
        if not visited[node]:
            if DFS(node, visited, parent, graph):
                return True
    return False

num_nodes = int(input("Nhập số đỉnh của đồ thị: "))
graph = {}

for i in range(num_nodes):
    print("Nhập các đỉnh kề của đỉnh", i, "(cách nhau bằng dấu cách, nhập -1 để kết thúc):")
    neighbors = list(map(int, input().split()))
    if -1 in neighbors:
        neighbors.remove(-1)
    graph[i] = neighbors

print("Đồ thị:", graph)

if ChuTrinh(graph):
    print("Đồ thị có chu trình.")
else:
    print("Đồ thị không có chu trình.")