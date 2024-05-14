def BFS(node, visited, graph):
    queue = [node]
    visited[node] = True
    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def SoThanhPhan(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    count = 0
    
    for node in range(num_nodes):
        if not visited[node]:
            BFS(node, visited, graph)
            count += 1
    
    return count

num_nodes = int(input("Nhập số đỉnh của đồ thị: "))
graph = {}

for i in range(num_nodes):
    print("Nhập các đỉnh kề của đỉnh", i, "(cách nhau bằng dấu cách, nhập -1 để kết thúc):")
    neighbors = list(map(int, input().split()))
    if -1 in neighbors:
        neighbors.remove(-1)
    graph[i] = neighbors

print("Đồ thị:", graph)

print("Số thành phần liên thông của đồ thị:", SoThanhPhan(graph))