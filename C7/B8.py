def DFS(graph, start, end, visited):
    visited[start] = True

    if start == end:
        return True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            if DFS(graph, neighbor, end, visited):
                return True
    return False

def DuongDi(graph, v1, v2):
    num_nodes = len(graph)
    visited = [False] * num_nodes

    return DFS(graph, v1, v2, visited)

num_nodes = int(input("Nhập số đỉnh của đồ thị: "))
graph = {}

for i in range(num_nodes):
    print("Nhập các đỉnh kề của đỉnh", i, "(cách nhau bằng dấu cách, nhập -1 để kết thúc):")
    neighbors = list(map(int, input().split()))
    if -1 in neighbors:
        neighbors.remove(-1)
    graph[i] = neighbors

print("Đồ thị:", graph)

v1 = int(input("Nhập đỉnh v1: "))
v2 = int(input("Nhập đỉnh v2: "))

if DuongDi(graph, v1, v2):
    print("Có đường đi từ đỉnh", v1, "đến đỉnh", v2)
else:
    print("Không có đường đi từ đỉnh", v1, "đến đỉnh", v2)